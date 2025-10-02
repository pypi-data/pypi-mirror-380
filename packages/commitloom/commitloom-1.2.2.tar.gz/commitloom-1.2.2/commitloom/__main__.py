#!/usr/bin/env python3
"""Entry point for running commitloom as a module."""

import os
import sys

import click
from dotenv import load_dotenv

# Load environment variables before any imports
env_path = os.path.join(os.path.dirname(__file__), "..", ".env")
print(f"Loading .env from: {os.path.abspath(env_path)}")
load_dotenv(dotenv_path=env_path)

# Debug: Check if API key is loaded
api_key = os.getenv("OPENAI_API_KEY")
print(f"API Key loaded: {'Yes' if api_key else 'No'}")

from .cli import console
from .cli.cli_handler import CommitLoom


def handle_error(error: BaseException) -> None:
    """Handle errors in a consistent way."""
    if isinstance(error, KeyboardInterrupt):
        console.print_error("\nOperation cancelled by user.")
    else:
        console.print_error(f"An error occurred: {str(error)}")


@click.group()
@click.option("-d", "--debug", is_flag=True, help="Enable debug logging")
@click.pass_context
def cli(ctx, debug: bool) -> None:
    """Create structured git commits with AI-generated messages."""
    ctx.ensure_object(dict)
    ctx.obj["DEBUG"] = debug
    
    if debug:
        console.setup_logging(debug=True)


@cli.command(help="Generate an AI-powered commit message and commit your changes")
@click.option("-y", "--yes", is_flag=True, help="Skip all confirmation prompts")
@click.option("-c", "--combine", is_flag=True, help="Combine all changes into a single commit")
@click.pass_context
def commit(ctx, yes: bool, combine: bool) -> None:
    """Generate commit message and commit changes."""
    debug = ctx.obj.get("DEBUG", False)
    
    try:
        # Use test_mode=True when running tests (detected by pytest)
        test_mode = "pytest" in sys.modules
        # Only pass API key if not in test mode and it exists
        api_key = None if test_mode else os.getenv("OPENAI_API_KEY")

        # Initialize with test_mode
        loom = CommitLoom(test_mode=test_mode, api_key=api_key if api_key else None)
        loom.run(auto_commit=yes, combine_commits=combine, debug=debug)
    except (KeyboardInterrupt, Exception) as e:
        handle_error(e)
        sys.exit(1)


@cli.command(help="Show usage statistics and metrics")
@click.pass_context
def stats(ctx) -> None:
    """Show usage statistics."""
    debug = ctx.obj.get("DEBUG", False)
    
    try:
        # Create a CommitLoom instance and run the stats command
        loom = CommitLoom(test_mode=True)  # Test mode to avoid API key requirement
        if debug:
            console.setup_logging(debug=True)
        loom.stats_command()
    except (KeyboardInterrupt, Exception) as e:
        handle_error(e)
        sys.exit(1)


# For backwards compatibility, default to commit command if no subcommand provided
def main() -> None:
    """Entry point for the CLI."""
    # Check if the first argument is a known command, if not, insert 'commit'
    known_commands = ['commit', 'stats']
    
    if len(sys.argv) > 1 and not sys.argv[1].startswith('-') and sys.argv[1] not in known_commands:
        sys.argv.insert(1, 'commit')
    
    # If no arguments provided, add 'commit' as the default command
    if len(sys.argv) == 1:
        sys.argv.append('commit')
        
    cli(obj={})


if __name__ == "__main__":
    main()
