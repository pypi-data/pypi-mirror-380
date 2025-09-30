import asyncio
import logging
import sys
from pathlib import Path

import click
from yaspin import yaspin
import yaml
from . import co_datascientist_api, mcp_local_server
from .settings import settings
from .workflow_runner import workflow_runner
from .cloud_utils.databricks_utils import get_code_from_databricks_config
from .plotting.plot_kpi_progression import main as plot_kpi_main, parse_arguments as plot_kpi_parse_args
from .plotting.python_diff_pdf_simple import SimpleDiffPDFGenerator

def ensure_keyring_works():
    """
    Ensure that keyring backend works; fall back to plaintext file if not.
    """
    try:
        import keyring
        test_service = "test_service"
        test_username = "test_user"
        test_password = "test_password"
        keyring.set_password(test_service, test_username, test_password)
        retrieved = keyring.get_password(test_service, test_username)
        keyring.delete_password(test_service, test_username)
        if retrieved == test_password:
            return
    except Exception:
        pass
    try:
        import keyring
        import keyrings.alt.file
        keyring.set_keyring(keyrings.alt.file.PlaintextKeyring())
        click.echo("Using file-based keyring for secure storage")
    except ImportError:
        click.echo("Please install keyrings.alt: pip install keyrings.alt")
        sys.exit(1)


def print_section_header(title: str):
    click.echo(f"\n{title}")
    click.echo("─" * len(title))


def print_success(message: str):
    click.echo(f"SUCCESS: {message}")


def print_info(message: str):
    click.echo(f"INFO: {message}")


def print_warning(message: str):
    click.echo(f"WARNING: {message}")


def print_error(message: str):
    click.echo(f"ERROR: {message}")


def print_logo():
    """Print the awesome Tropiflo ASCII logo in blue with tagline"""
    # Use print() instead of click.echo() to preserve ANSI colors
    BLUE = '\033[94m'
    RESET = '\033[0m'

    print(f"""
{BLUE}$$$$$$$$\\                            $$\\  $$$$$$\\  $$\\           
\\__$$  __|                           \\__|$$  __$$\\ $$ |          
   $$ | $$$$$$\\   $$$$$$\\   $$$$$$\\  $$\\ $$ /  \\__|$$ | $$$$$$\\  
   $$ |$$  __$$\\ $$  __$$\\ $$  __$$\\ $$ |$$$$\\     $$ |$$  __$$\\ 
   $$ |$$ |  \\__|$$ /  $$ |$$ /  $$ |$$ |$$  _|    $$ |$$ /  $$ |
   $$ |$$ |      $$ |  $$ |$$ |  $$ |$$ |$$ |      $$ |$$ |  $$ |
   $$ |$$ |      \\$$$$$$  |$$$$$$$  |$$ |$$ |      $$ |\\$$$$$$  |
   \\__|\\__|       \\______/ $$  ____/ \\__|\\__|      \\__| \\______/ 
                           $$ |                                  
                           $$ |                                  
                           \\__|{RESET}

{BLUE}>{RESET} lets explore this problem!""")


@click.group()
@click.option('--reset-openai-key', is_flag=True, help='Reset the OpenAI API key')
@click.pass_context
def main(ctx, reset_openai_key: bool):
    # Initialize keyring and logging
    ensure_keyring_works()
    logging.basicConfig(level=settings.log_level)
    logging.info(f"settings: {settings.model_dump()}")

    print_logo()

    # Reset OpenAI key if requested
    if reset_openai_key:
        settings.delete_openai_key()
        print_success("OpenAI key removed. Using free tier.")

    # Ensure API key exists for all commands except token management
    if ctx.invoked_subcommand not in ('set-token', 'openai-key'):
        try:
            settings.get_api_key()
            if not settings.api_key or not settings.api_key.get_secret_value():
                print_error("No API key found. Please run 'set-token' to configure your API key.")
                sys.exit(1)
        except Exception as e:
            print_error(f"Error loading API key: {e}")
            sys.exit(1)


@main.command()
def mcp_server():
    """Start the local MCP server"""
    print_section_header("MCP Server")
    print_info("Starting MCP server... Press Ctrl+C to exit.")
    asyncio.run(mcp_local_server.run_mcp_server())


@main.command()
@click.option('--token', required=False, help='Your API key (if not provided, you will be prompted)')
def set_token(token):
    """Set your Co-DataScientist API key"""
    from pydantic import SecretStr

    print_section_header("Set API Key")
    if not token:
        token = click.prompt("Please enter your API key", hide_input=True)
    if not token:
        print_error("No API key provided. Aborting.")
        return

    settings.api_key = SecretStr(token)
    try:
        asyncio.run(co_datascientist_api.test_connection())
        print_success("Token validated successfully!")
    except Exception as e:
        print_error(f"Token validation failed: {e}")
        return

    try:
        import keyring
        keyring.set_password(settings.service_name, "user", token)
        print_success("API key saved and will be remembered between sessions!")
    except Exception as e:
        print_error(f"Failed to save API key: {e}")
        print_info("You can set the CO_DATASCIENTIST_API_KEY environment variable for persistence.")


@main.command()
@click.option('--script-path', required=False, type=click.Path(exists=True), help='Absolute path to the python code to improve')
@click.option('--cloud-config', required=False, type=click.Path(exists=True), help='Path to cloud config file (mutually exclusive with --script-path)')
@click.option('--python-path', required=False, type=click.Path(), default=sys.executable, show_default=True, help='Path to the python interpreter to use')
@click.option('--parallel', required=False, type=int, default=1, show_default=True, help='Number of code versions to run concurrently')
# @click.option('--no-preflight', is_flag=True, help='Disable preflight Q&A (enabled by default)')
@click.option('--use-cached-qa', is_flag=True, help='Use cached Q&A answers instead of prompting (implies preflight enabled)')
@click.option('--debug', is_flag=True, help='Show detailed logs')

# TODO: need a way to check we have a specific script path or cloud path...

def run(script_path, python_path, parallel, debug, cloud_config, use_cached_qa):
    """Run the workflow on your script"""
    try:
        # if databricks or gcloud we need to grab the code from the cloud config to have as a string locally like the input local code.
        if cloud_config:
            #how to read a yaml file to an object?
            with open(cloud_config, 'r') as file:
                config = yaml.safe_load(file)

            if 'databricks' in config:
                # TODO: find a way to get the baseline code from the cloud!
                baseline_code = get_code_from_databricks_config(config['databricks']['code_path']) #TODO: check over.
                project_path = config['databricks']['volume_uri'] #TODO:  check over. not needed for POC.
            elif 'gcloud' in config:
                # For GCloud, get baseline code from local script path
                script_path = config['gcloud'].get('script_path')
                if not script_path:
                    print_error("GCloud config must specify 'script_path' for baseline code. Aborting.")
                    return
                baseline_code = Path(script_path).read_text()
                project_path = Path(script_path).parent
            else:
                print_error("Cloud config must contain either 'databricks' or 'gcloud' configuration. Aborting.")
                return
        elif script_path:
            baseline_code = Path(script_path).read_text()
            project_path = Path(script_path).parent
            # Set default config for local script runs (no cloud integration)
            config = {'databricks': False}
        else:
            print_error("No script path or cloud config provided. Aborting.")
            return
        
        if not debug:
            click.echo()
        with yaspin(text="Initializing workflow...", color="magenta") as spinner:
            asyncio.run(
                workflow_runner.run_workflow(
                    baseline_code, python_path, project_path, {**config, 'parallel': max(1, int(parallel or 1)), 'use_cached_qa': use_cached_qa}, spinner, debug
                )
            )
        click.echo()
    except Exception as e:
        msg = str(e)
        import traceback
        print(f"DEBUG: Full exception: {e}")
        print(f"DEBUG: Exception type: {type(e)}")
        traceback.print_exc()
        if "Unauthorized" in msg or "401" in msg:
            print_error("Authentication failed. Please run 'set-token' again.")
        else:
            print_error(f"Error running workflow: {e}")


def _costs_disabled():
    return None


@main.command()
def status():
    """Show current usage status"""
    try:
        with yaspin(text="Checking status...", color="yellow") as spinner:
            status = asyncio.run(co_datascientist_api.get_user_usage_status())
        print_section_header("Usage Status")
    except Exception as e:
        msg = str(e)
        if "Unauthorized" in msg or "401" in msg:
            print_error("Authentication failed. Please run 'set-token' again.")
        else:
            print_error(f"Error fetching status: {e}")


@main.command()
@click.option('--remove', is_flag=True, help='Remove stored OpenAI key')
def openai_key(remove):
    """Manage your OpenAI API key for unlimited usage"""
    print_section_header("OpenAI Key Management")
    if remove:
        settings.delete_openai_key()
        print_success("OpenAI key removed. Using free tier.")
    else:
        current = settings.get_openai_key(prompt_if_missing=False)
        if current:
            print_success("OpenAI key is currently configured.")
            print_info("Your requests use your OpenAI account for unlimited usage.")
            print_info("Use '--remove' flag to switch back to free tier.")
        else:
            print_info("No OpenAI key configured. Using free tier.")
            settings.get_openai_key(prompt_if_missing=True)


@main.command()
@click.option('--checkpoints-dir', '-c', required=True, type=click.Path(exists=True), 
              help='Directory containing the checkpoint JSON files')
@click.option('--max-iteration', '-m', type=int, default=None,
              help='Maximum iteration to include in the plot (default: include all iterations)')
@click.option('--title', '-t', type=str, default='RMSE Progression Over Iterations',
              help='Title for the plot')
@click.option('--output', '-o', type=str, default=None,
              help='Output file path for the plot (default: auto-generated based on parameters)')
@click.option('--kpi-label', '-k', type=str, default='RMSE',
              help='Label for the KPI metric (default: "RMSE")')
def plot_kpi(checkpoints_dir, max_iteration, title, output, kpi_label):
    """Plot KPI progression from checkpoint JSON files"""
    print_section_header("KPI Progression Plot")
    
    try:
        # Import the plotting functions
        from .plotting.plot_kpi_progression import load_kpi_data, create_plot
        import os
        
        # Validate checkpoint directory
        if not os.path.exists(checkpoints_dir):
            print_error(f"Checkpoint directory not found: {checkpoints_dir}")
            return
        
        print_info(f"Loading KPI data from: {checkpoints_dir}")
        if max_iteration:
            print_info(f"Limiting to iterations <= {max_iteration}")
        print_info("Auto-converting negative KPI values to positive for better visualization")
        
        # Load data
        data = load_kpi_data(checkpoints_dir, max_iteration)
        
        if not data:
            print_error("No valid data found in JSON files!")
            return
        
        print_info(f"Found {len(data)} data points")
        
        # Generate output filename if not provided
        if output is None:
            base_name = "kpi_progression"
            if max_iteration:
                base_name += f"_max{max_iteration}"
            # Clean title for filename
            title_clean = "".join(c for c in title if c.isalnum() or c in (' ', '-', '_')).strip()
            title_clean = title_clean.replace(' ', '_').lower()
            if title_clean and title_clean != "rmse_progression_over_iterations":
                base_name += f"_{title_clean}"
            output_path = f"{base_name}_plot.png"
        else:
            output_path = output
        
        # Create the plot
        create_plot(data, title, kpi_label, output_path)
        print_success(f"KPI progression plot saved to: {output_path}")
        
    except Exception as e:
        print_error(f"Error creating KPI plot: {e}")


@main.command()
@click.argument('file1', type=click.Path(exists=True))
@click.argument('file2', type=click.Path(exists=True))
@click.option('--output', '-o', type=str, default=None,
              help='Output PDF file path (default: auto-generated from title)')
@click.option('--title', '-t', type=str, default='Beautiful Python Diff',
              help='Custom title for the diff report')
def diff_pdf(file1, file2, output, title):
    """Create a beautiful PDF diff between two Python files"""
    print_section_header("Python Diff PDF Generator")
    
    try:
        # Validate files exist
        file1_path = Path(file1)
        file2_path = Path(file2)
        
        if not file1_path.exists():
            print_error(f"File '{file1}' not found")
            return
        
        if not file2_path.exists():
            print_error(f"File '{file2}' not found")
            return
        
        print_info(f"Comparing files:")
        print_info(f"   Baseline: {file1}")
        print_info(f"   Modified: {file2}")
        print_info(f"Generating beautiful PDF diff...")
        
        # Create diff
        generator = SimpleDiffPDFGenerator()
        output_path = generator.create_pdf_diff(str(file1_path), str(file2_path), output, title)
        
        print_success(f"PDF diff saved as '{output_path}'")
        
    except Exception as e:
        print_error(f"Error creating PDF diff: {e}")


if __name__ == '__main__':
    main()
