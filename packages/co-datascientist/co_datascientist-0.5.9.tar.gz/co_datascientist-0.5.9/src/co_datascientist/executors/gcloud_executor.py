"""Google Cloud Run Jobs executor."""

import asyncio
import base64
import logging
import platform
import subprocess
import time
import uuid
from typing import Dict, Any, Optional, List, Tuple

from .base_executor import BaseExecutor
from ..models import CodeResult, CodeVersion


class GCloudExecutor(BaseExecutor):
    """Executor for running Python code on Google Cloud Run Jobs."""
    
    @property
    def platform_name(self) -> str:
        return "gcloud"
    
    def __init__(self, python_path: str = "python", config: Dict[str, Any] = None):
        super().__init__(python_path, config)
        
        # Extract gcloud configuration with sensible defaults
        gcloud_config = config.get('gcloud', {}) if config else {}
        
        self.job_template = gcloud_config.get('job_template', 'default-job')
        self.region = gcloud_config.get('region', 'europe-west3')
        self.base_args = gcloud_config.get('base_args', [])
        self.timeout = gcloud_config.get('timeout', '30m')
        self.code_injection_method = gcloud_config.get('code_injection_method', 'args')
        
        # Distributed execution configuration (auto-enabled for parallel execution)
        self.polling_interval = gcloud_config.get('polling_interval', 5)
        self.max_concurrent_jobs = gcloud_config.get('max_concurrent_jobs', 100)
        
        # Platform-specific configuration
        self.is_windows = platform.system().lower() == 'windows'
        self.gcloud_path = self._get_gcloud_path()
    
    def _get_gcloud_path(self) -> str:
        """Get the gcloud path, handling Windows PowerShell if needed."""
        if self.is_windows:
            try:
                # Use PowerShell to get gcloud path on Windows
                result = subprocess.run(
                    ["PowerShell", "-Command", "(Get-command gcloud).source"],
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                if result.returncode == 0:
                    return result.stdout.strip()
                else:
                    logging.warning(f"Failed to get gcloud path via PowerShell: {result.stderr}")
                    return "gcloud"  # Fallback to default
            except Exception as e:
                logging.warning(f"Error getting gcloud path on Windows: {e}")
                return "gcloud"  # Fallback to default
        else:
            return "gcloud"  # Default for Unix-like systems
    
    def _build_gcloud_command(self, base_args: List[str]) -> List[str]:
        """Build gcloud command with platform-specific handling."""
        if self.is_windows and self.gcloud_path != "gcloud":
            return ["powershell", "-File", self.gcloud_path] + base_args
        else:
            return ["gcloud"] + base_args
    
    def execute(self, code: str) -> CodeResult:
        """Execute Python code on Google Cloud Run Jobs.
        
        Args:
            code: Python code to execute
            
        Returns:
            CodeResult containing stdout, stderr, return_code, and runtime_ms
        """
        logging.info(f"GCloud Job Template: {self.job_template}")
        logging.info(f"GCloud Region: {self.region}")
        logging.info(f"GCloud Timeout: {self.timeout}")
        logging.info(f"Code injection method: {self.code_injection_method}")
        
        t0 = time.time()
        
        # Create unique execution identifier
        execution_id = f"{int(t0)}_{uuid.uuid4().hex[:8]}"
        
        # Encode code for safe transmission via command args
        code_b64 = base64.b64encode(code.encode('utf-8')).decode('ascii')
        
        logging.info(f"Injecting code via args (length: {len(code)} chars)")

        # Build args with Windows-specific escaping
        if self.is_windows:
            # Windows requires additional escaping and quotes
            args_param = f'--args=python,-c,\'import sys; import base64; exec(base64.b64decode(\\"{code_b64}\\").decode(\\"utf-8\\"))\''
        else:
            # Unix/Linux standard escaping
            args_param = f'--args=-c,import sys; import base64; exec(base64.b64decode("{code_b64}").decode("utf-8"))'

        # Execute GCloud job synchronously using platform-specific command
        base_cmd = [
            'run', 'jobs', 'execute', self.job_template,
            f'--region={self.region}',
            '--wait',  # Wait for job completion
            '--format=value(metadata.name)',  # Get the execution name
            args_param
        ]
        cmd = self._build_gcloud_command(base_cmd)

        logging.info(f"Executing gcloud command: {' '.join(cmd[:6])}... [code injection args hidden]")
        
        try:
            # Execute job and wait for completion
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=1800  # 30 minute timeout for job execution
            )

            runtime_ms = int((time.time() - t0) * 1000)

            if result.returncode != 0:
                # GCloud command failed - extract just the essential error info
                stderr_lines = result.stderr.strip().split('\n') if result.stderr else []
                # Look for the actual error message (usually contains "ERROR:")
                error_line = None
                for line in stderr_lines:
                    if "ERROR:" in line and "gcloud.run.jobs.execute" in line:
                        error_line = line.strip()
                        break
                
                if error_line:
                    error_msg = f"GCloud job execution failed: {error_line}"
                else:
                    error_msg = f"GCloud job execution failed (return code {result.returncode})"
                
                logging.error(f"GCloud execution failed with return code {result.returncode}")
                return CodeResult(
                    stdout=None, 
                    stderr=error_msg, 
                    return_code=result.returncode, 
                    runtime_ms=runtime_ms
                )

            # Extract execution name
            execution_name = result.stdout.strip()
            logging.info(f"GCloud job execution completed: {execution_name}")

            # Retrieve logs with retry logic for timing issues
            logs = self._get_job_logs_with_retry(execution_name, execution_id)

            if logs:
                logging.info(f"Successfully retrieved job logs: {logs[:100]}...")  # Log first 100 chars
                return CodeResult(
                    stdout=logs,
                    stderr=None,
                    return_code=0,
                    runtime_ms=runtime_ms
                )
            else:
                logging.warning("No logs retrieved from job execution after retries")
                return CodeResult(
                    stdout="Job completed successfully (no logs available)",
                    stderr=None,
                    return_code=0,
                    runtime_ms=runtime_ms
                )

        except subprocess.TimeoutExpired:
            # Handle timeout gracefully
            runtime_ms = int((time.time() - t0) * 1000)
            error_msg = f"GCloud job execution timed out after 30 minutes"
            logging.info(error_msg)
            return CodeResult(
                stdout=None, 
                stderr=error_msg, 
                return_code=-9, 
                runtime_ms=runtime_ms
            )
        
        except Exception as e:
            # Handle any other errors
            runtime_ms = int((time.time() - t0) * 1000)
            logging.error(f"GCloud job execution error: {e}")
            return CodeResult(
                stdout=None, 
                stderr=f"GCloud execution error: {e}", 
                return_code=1, 
                runtime_ms=runtime_ms
            )
    
    def _get_job_logs_with_retry(self, execution_name: str, execution_id: str) -> Optional[str]:
        """Retrieve logs with retry logic to handle timing issues.
        
        Args:
            execution_name: Name of the specific execution
            execution_id: Unique execution identifier for log filtering
            
        Returns:
            Job logs as string, or None if logs couldn't be retrieved after retries
        """
        max_retries = 3
        retry_delays = [2, 5, 10]  # seconds to wait between retries
        
        for attempt in range(max_retries):
            logs = self._get_job_logs(execution_name, execution_id)
            if logs:
                return logs
            
            if attempt < max_retries - 1:  # Don't sleep after last attempt
                delay = retry_delays[attempt]
                logging.info(f"No logs found on attempt {attempt + 1}/{max_retries}, retrying in {delay}s...")
                time.sleep(delay)
        
        logging.warning(f"Failed to retrieve logs after {max_retries} attempts")
        return None
    
    def _get_job_logs(self, execution_name: str, execution_id: str) -> Optional[str]:
        """Retrieve logs from a completed GCloud Run Job execution.

        Args:
            execution_name: Name of the specific execution (e.g., 'test-job-clean-abc123')
            execution_id: Unique execution identifier for log filtering

        Returns:
            Job logs as string, or None if logs couldn't be retrieved
        """
        try:
            logging.info(f"Retrieving logs for execution: {execution_name}")

            # Try multiple log retrieval strategies for better reliability
            logs = self._try_multiple_log_strategies(execution_name)
            if logs:
                return logs
            
            logging.warning("All log retrieval strategies failed")
            return None
            
        except Exception as e:
            logging.error(f"Error retrieving GCloud job logs: {e}")
            return None

    def _try_multiple_log_strategies(self, execution_name: str) -> Optional[str]:
        """Try multiple strategies to retrieve logs, as different approaches work better in different scenarios."""
        
        # Strategy 1: Standard approach with stdout filter
        logs = self._get_logs_with_filter(execution_name, "stdout")
        if logs:
            logging.info("Retrieved logs using stdout filter strategy")
            return logs
        
        # Strategy 2: Try stderr filter
        logs = self._get_logs_with_filter(execution_name, "stderr")
        if logs:
            logging.info("Retrieved logs using stderr filter strategy")
            return logs
        
        # Strategy 3: Try broader filter without log name restriction
        logs = self._get_logs_broad_filter(execution_name)
        if logs:
            logging.info("Retrieved logs using broad filter strategy")
            return logs
        
        # Strategy 4: Try with longer freshness window
        logs = self._get_logs_with_filter(execution_name, "stdout", freshness="1h")
        if logs:
            logging.info("Retrieved logs using extended freshness strategy")
            return logs
        
        return None
    
    def _get_logs_with_filter(self, execution_name: str, log_type: str = "stdout", freshness: str = "15m") -> Optional[str]:
        """Get logs with specific filter."""
        try:
            # Build log filter with Windows-specific escaping
            if self.is_windows:
                log_filter = f'resource.type="cloud_run_job" logName=~\\"{log_type}\\" labels.\\"run.googleapis.com/execution_name\\"=\\"{execution_name}\\"'
            else:
                log_filter = f'resource.type="cloud_run_job" logName=~"{log_type}" labels."run.googleapis.com/execution_name"="{execution_name}"'
            
            base_cmd = [
                'logging', 'read',
                log_filter,
                '--limit=100',
                '--format=value(textPayload)',
                f'--freshness={freshness}'
            ]
            cmd = self._build_gcloud_command(base_cmd)

            logging.info(f"Executing log command: {' '.join(cmd[:4])}...")
            logs_result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)

            if logs_result.returncode == 0 and logs_result.stdout.strip():
                return logs_result.stdout.strip()
            else:
                return None
                
        except Exception as e:
            logging.error(f"Error in _get_logs_with_filter: {e}")
            return None
    
    def _get_logs_broad_filter(self, execution_name: str) -> Optional[str]:
        """Get logs with a broader filter that doesn't restrict log type."""
        try:
            # Broader filter - just match the execution name without log type restriction
            if self.is_windows:
                log_filter = f'resource.type="cloud_run_job" labels.\\"run.googleapis.com/execution_name\\"=\\"{execution_name}\\"'
            else:
                log_filter = f'resource.type="cloud_run_job" labels."run.googleapis.com/execution_name"="{execution_name}"'
            
            base_cmd = [
                'logging', 'read',
                log_filter,
                '--limit=100',
                '--format=value(textPayload)',
                '--freshness=30m'
            ]
            cmd = self._build_gcloud_command(base_cmd)

            logging.info(f"Executing broad log command: {' '.join(cmd[:4])}...")
            logs_result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)

            if logs_result.returncode == 0 and logs_result.stdout.strip():
                return logs_result.stdout.strip()
            else:
                return None
                
        except Exception as e:
            logging.error(f"Error in _get_logs_broad_filter: {e}")
            return None
    
    def is_available(self) -> bool:
        """Check if gcloud CLI is available and configured."""
        try:
            cmd = self._build_gcloud_command(['version'])
            result = subprocess.run(
                cmd, 
                capture_output=True, 
                timeout=10
            )
            return result.returncode == 0
        except (subprocess.SubprocessError, FileNotFoundError):
            return False

    # Distributed execution methods
    
    def supports_distributed_execution(self) -> bool:
        """Check if this executor supports distributed batch execution."""
        return self.is_available()

    async def execute_batch_distributed(self, code_versions: List[CodeVersion]) -> List[CodeResult]:
        """Execute a batch of code versions using true distributed execution.
        
        This method submits all jobs asynchronously to Google Cloud Run Jobs,
        then polls for completion. Each job runs on a separate container.
        
        Args:
            code_versions: List of CodeVersion objects to execute
            
        Returns:
            List of CodeResult objects in the same order as input
        """
        if not self.supports_distributed_execution():
            raise RuntimeError("Distributed execution not supported or gcloud not available")
        
        if len(code_versions) > self.max_concurrent_jobs:
            logging.warning(f"Batch size {len(code_versions)} exceeds max_concurrent_jobs {self.max_concurrent_jobs}")
        
        logging.info(f"Starting distributed execution of {len(code_versions)} jobs on Google Cloud")
        
        
        # Submit all jobs asynchronously
        job_submissions = await self._submit_jobs_async(code_versions)
        
        logging.info(f"Job submissions completed: {len(job_submissions)} jobs submitted")
        
        # Poll for results
        results = await self._poll_job_results(job_submissions)
        
        logging.info(f"Completed distributed execution: {len(results)} results")
        
        logging.info(f"Completed distributed execution of {len(results)} jobs")
        return results

    async def _submit_jobs_async(self, code_versions: List[CodeVersion]) -> List[Tuple[str, str, float]]:
        """Submit all jobs asynchronously and return job tracking information.
        
        Args:
            code_versions: List of CodeVersion objects to submit
            
        Returns:
            List of tuples: (code_version_id, execution_name, start_time)
        """
        job_submissions = []
        
        for cv in code_versions:
            try:
                execution_name = await self._submit_single_job(cv.code)
                start_time = time.time()
                job_submissions.append((cv.code_version_id, execution_name, start_time))
                logging.info(f"Submitted job {execution_name} for code version {cv.code_version_id}")
                
            except Exception as e:
                logging.error(f"Failed to submit job for code version {cv.code_version_id}: {e}")
                # Create a failed result for this job
                job_submissions.append((cv.code_version_id, None, time.time()))
        
        return job_submissions

    async def _submit_single_job(self, code: str) -> str:
        """Submit a single job asynchronously (without --wait flag).
        
        Args:
            code: Python code to execute
            
        Returns:
            execution_name: The name of the submitted execution
        """
        code_b64 = base64.b64encode(code.encode('utf-8')).decode('ascii')
        
        # Build args with Windows-specific escaping
        if self.is_windows:
            # Windows requires additional escaping and quotes
            args_param = f'--args=python,-c,\'import sys; import base64; exec(base64.b64decode(\\"{code_b64}\\").decode(\\"utf-8\\"))\''
        else:
            # Unix/Linux standard escaping
            args_param = f'--args=-c,import sys; import base64; exec(base64.b64decode("{code_b64}").decode("utf-8"))'
        
        # Submit job WITHOUT --wait flag for async execution
        base_cmd = [
            'run', 'jobs', 'execute', self.job_template,
            f'--region={self.region}',
            # Note: NO --wait flag here - this makes it asynchronous
            '--format=value(metadata.name)',
            args_param
        ]
        cmd = self._build_gcloud_command(base_cmd)
        
        # Run in thread pool to avoid blocking
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(
            None, 
            lambda: subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        )
        
        if result.returncode != 0:
            raise RuntimeError(f"Job submission failed: {result.stderr}")
        
        execution_name = result.stdout.strip()
        return execution_name

    async def _poll_job_results(self, job_submissions: List[Tuple[str, str, float]]) -> List[CodeResult]:
        """Poll all submitted jobs until completion and collect results.
        
        Args:
            job_submissions: List of (code_version_id, execution_name, start_time) tuples
            
        Returns:
            List of CodeResult objects in the same order as job_submissions
        """
        results = {}
        failed_submissions = set()
        
        # Track jobs that failed to submit
        for cv_id, execution_name, start_time in job_submissions:
            if execution_name is None:
                results[cv_id] = CodeResult(
                    stdout=None,
                    stderr="Job submission failed",
                    return_code=1,
                    runtime_ms=0
                )
                failed_submissions.add(cv_id)
        
        # Poll remaining jobs
        pending_jobs = [(cv_id, exec_name, start_time) for cv_id, exec_name, start_time in job_submissions 
                       if cv_id not in failed_submissions]
        
        max_wait_time = 1800  # 30 minutes timeout
        start_polling_time = time.time()
        
        while pending_jobs:
            # Check for overall timeout
            if time.time() - start_polling_time > max_wait_time:
                logging.error(f"Polling timeout after {max_wait_time} seconds, marking remaining jobs as failed")
                for cv_id, execution_name, start_time in pending_jobs:
                    runtime_ms = int((time.time() - start_time) * 1000)
                    results[cv_id] = CodeResult(
                        stdout=None,
                        stderr="Job polling timeout",
                        return_code=-1,
                        runtime_ms=runtime_ms
                    )
                break
                
            completed_jobs = []
            
            logging.info(f"Polling {len(pending_jobs)} jobs...")
            
            for cv_id, execution_name, start_time in pending_jobs:
                try:
                    status = await self._check_job_status(execution_name)
                    logging.info(f"Job {execution_name}: status = {status}")
                    
                    if status in ['Ready', 'Succeeded', 'Completed']:
                        # Job completed successfully
                        logs = await self._get_job_logs_async(execution_name)
                        runtime_ms = int((time.time() - start_time) * 1000)
                        
                        # Extract KPI from logs
                        from ..kpi_extractor import extract_kpi_from_stdout
                        kpi_value = extract_kpi_from_stdout(logs)
                        
                        
                        results[cv_id] = CodeResult(
                            stdout=logs,
                            stderr=None,
                            return_code=0,
                            runtime_ms=runtime_ms,
                            kpi=kpi_value
                        )
                        completed_jobs.append((cv_id, execution_name, start_time))
                        logging.info(f"Job {execution_name} completed successfully")
                        
                    elif status in ['Failed', 'Error', 'Cancelled']:
                        # Job failed
                        runtime_ms = int((time.time() - start_time) * 1000)
                        error_logs = await self._get_job_logs_async(execution_name)
                        
                        results[cv_id] = CodeResult(
                            stdout=None,
                            stderr=error_logs or "Job execution failed",
                            return_code=1,
                            runtime_ms=runtime_ms
                        )
                        completed_jobs.append((cv_id, execution_name, start_time))
                        logging.error(f"Job {execution_name} failed with status {status}")
                        
                    elif status in ['Running', 'Executing', 'Unknown']:
                        # Job still running, continue polling
                        job_runtime = time.time() - start_time
                        if job_runtime > 1200:  # 20 minute individual job timeout
                            logging.warning(f"Job {execution_name} running for {job_runtime:.1f}s, marking as timeout")
                            results[cv_id] = CodeResult(
                                stdout=None,
                                stderr="Individual job timeout",
                                return_code=-1,
                                runtime_ms=int(job_runtime * 1000)
                            )
                            completed_jobs.append((cv_id, execution_name, start_time))
                        else:
                            logging.info(f"Job {execution_name} still running ({job_runtime:.1f}s)")
                    else:
                        logging.warning(f"Job {execution_name} has unexpected status: {status}")
                    
                except Exception as e:
                    logging.error(f"Error checking status for job {execution_name}: {e}")
                    # Continue polling this job
            
            # Remove completed jobs from pending list
            for completed_job in completed_jobs:
                pending_jobs.remove(completed_job)
            
            # Wait before next polling cycle
            if pending_jobs:
                logging.info(f"Waiting {self.polling_interval}s before next poll...")
                await asyncio.sleep(self.polling_interval)
        
        # Return results in the same order as job_submissions
        ordered_results = []
        for cv_id, _, _ in job_submissions:
            ordered_results.append(results[cv_id])
        
        return ordered_results

    async def _check_job_status(self, execution_name: str) -> str:
        """Check the status of a specific job execution.
        
        Args:
            execution_name: Name of the execution to check
            
        Returns:
            Status string ('Ready', 'Running', 'Failed', etc.)
        """
        # Try to get both the condition type and the execution state
        base_cmd = [
            'run', 'jobs', 'executions', 'describe', execution_name,
            f'--region={self.region}',
            '--format=value(status.conditions[0].type,status.completionTime,status.startTime)'
        ]
        cmd = self._build_gcloud_command(base_cmd)
        
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(
            None,
            lambda: subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        )
        
        if result.returncode == 0:
            output = result.stdout.strip()
            parts = output.split('\t') if '\t' in output else [output]
            
            condition_type = parts[0] if parts else "Unknown"
            completion_time = parts[1] if len(parts) > 1 else ""
            start_time = parts[2] if len(parts) > 2 else ""
            
            # Log more detailed status info
            logging.info(f"Job {execution_name} - condition: {condition_type}, completed: {bool(completion_time)}, started: {bool(start_time)}")
            
            # If we have a completion time, the job is done
            if completion_time:
                # Check if it succeeded or failed by looking at the condition
                if condition_type in ['Ready', 'Completed']:
                    return 'Completed'
                else:
                    return 'Failed'
            elif start_time:
                return 'Running'
            else:
                return 'Pending'
        else:
            logging.warning(f"Failed to check status for {execution_name}: {result.stderr}")
            return "Unknown"

    async def _get_job_logs_async(self, execution_name: str) -> Optional[str]:
        """Asynchronously retrieve logs from a completed job execution.
        
        Args:
            execution_name: Name of the execution
            
        Returns:
            Job logs as string, or None if logs couldn't be retrieved
        """
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(
            None,
            lambda: self._get_job_logs_with_retry(execution_name, "")
        )
