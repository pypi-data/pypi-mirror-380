#!/usr/bin/env python3
"""
MCP Testing Framework CLI - Main entry point and command coordination
"""

import sys
import time

import click

from .. import __version__
from ..shared.console_shared import get_console
from ..utils.command_tracker import get_command_tracker
from .config_commands import (
    create_list_command,
    create_show_command,
)
from .create_commands import (
    create_create_group,
)
from .post_command_hooks import trigger_post_command_hooks
from .report_commands import (
    create_report_group,
)
from .setup_commands import (
    create_quickstart_group,
)

# Import command creators from modules
from .test_commands import (
    create_run_command,
)


def show_mcpt_overview():
    """Show ultra-simple overview"""
    console = get_console()
    console.print_header("MCP Testing (mcp-t) - Ultra-simple MCP server testing")
    console.console.print()
    console.console.print("[bold]Common commands:[/bold]")
    console.print_command("mcp-t quickstart", "Complete onboarding (demo + config)")
    console.print_command("mcp-t create suite", "Create test configurations")
    console.print_command("mcp-t create server", "Add server configurations")
    console.print_command("mcp-t run suite-id server-id", "Run tests")
    console.console.print()
    console.console.print("[dim]Use 'mcp-t --help' for all commands[/dim]")


@click.group(invoke_without_command=True, name="mcp-t")
@click.version_option(version=__version__, prog_name="mcp-t")
@click.option(
    "--no-update-notifier", is_flag=True, help="Disable version update notifications"
)
@click.option(
    "--no-report-suggestions", is_flag=True, help="Disable issue reporting suggestions"
)
@click.pass_context
def mcpt_cli(ctx, no_update_notifier, no_report_suggestions):
    """MCP Testing - Ultra-simple MCP server testing

    \\b
    Quick Commands:
      mcp-t quickstart               # Complete onboarding
      mcp-t create suite             # Create test suites
      mcp-t create server            # Add servers
      mcp-t run suite-id server-id   # Run tests
    """
    # Store flags in context for subcommands
    ctx.ensure_object(dict)
    ctx.obj["no_update_notifier"] = no_update_notifier
    ctx.obj["no_report_suggestions"] = no_report_suggestions

    # Track command start time for duration calculation
    ctx.obj["command_start_time"] = time.time()

    if ctx.invoked_subcommand is None:
        show_mcpt_overview()
        # Show notifications after main command (following update notifier pattern)
        trigger_post_command_hooks(ctx)


def mcpt_main():
    """Entry point for the ultra-simple mcp-t CLI"""
    # Store start time for command tracking (before try block to ensure it's always available)
    start_time = time.time()

    try:
        # Run the CLI
        mcpt_cli(standalone_mode=False)

        # Track successful command completion and show suggestions
        _handle_command_completion(start_time, exit_code=0)

    except click.BadParameter as e:
        # Handle parameter validation errors with user-friendly messages
        console = get_console()
        param_name = e.param.name if e.param else "parameter"

        # Extract the actual error message from Click's BadParameter
        error_msg = str(e).split(": ", 1)[-1] if ": " in str(e) else str(e)

        # Add suggestions if this is a choice parameter
        if hasattr(e.param, "type") and hasattr(e.param.type, "choices"):
            choices = list(e.param.type.choices)
            suggestions = [
                f"Try: mcp-t {' '.join(sys.argv[1:-1])} {choice}" for choice in choices
            ]
            console.print_error(f"Invalid {param_name}: {error_msg}", suggestions)
        else:
            console.print_error(f"Invalid {param_name}: {error_msg}")

        _handle_command_completion(start_time, exit_code=1)
        sys.exit(1)

    except click.UsageError as e:
        # Handle command not found and other usage errors
        console = get_console()

        # Extract command from message if it's a "No such command" error
        if "No such command" in str(e):
            # Try to extract the invalid command from the error message
            import re

            match = re.search(r"No such command '([^']+)'", str(e))
            if match:
                invalid_cmd = match.group(1)
                # Get available commands from the CLI
                available_commands = [
                    "quickstart",
                    "create",
                    "run",
                    "list",
                    "show",
                    "report",
                ]
                # Get suggestions from the existing suggestion system
                from .suggestions import find_closest_matches

                suggestions = find_closest_matches(
                    invalid_cmd, available_commands, max_suggestions=3, cutoff=0.5
                )

                if suggestions:
                    suggestion_list = [
                        f"Did you mean: mcp-t {suggestion}"
                        for suggestion in suggestions
                    ]
                    console.print_error(
                        f"Unknown command: '{invalid_cmd}'", suggestion_list
                    )
                else:
                    console.print_error(
                        f"Unknown command: '{invalid_cmd}'",
                        ["Try: mcp-t --help for all commands"],
                    )
            else:
                console.print_error(str(e))
        else:
            console.print_error(str(e))

        _handle_command_completion(start_time, exit_code=1)
        sys.exit(1)

    except SystemExit as e:
        # Handle CLI exits (including --help, errors, etc.)
        # SystemExit.code can be None, so provide default value
        exit_code = e.code if e.code is not None else 0
        _handle_command_completion(start_time, exit_code=exit_code)
        raise
    except Exception:
        # Handle unexpected errors
        _handle_command_completion(start_time, exit_code=1)
        raise


def _handle_command_completion(start_time: float, exit_code: int):
    """Track command completion and show suggestions"""
    try:
        # Track command for analytics
        duration_ms = (time.time() - start_time) * 1000
        command_name = " ".join(sys.argv) if sys.argv else "mcp-t"

        command_tracker = get_command_tracker()
        command_tracker.record_command(command_name, exit_code, duration_ms)

        # Show suggestions for all commands (not just failures)
        # Skip for help commands and version commands
        if not any(flag in sys.argv for flag in ["--help", "-h", "--version"]):
            ctx = click.get_current_context(silent=True)
            if ctx and hasattr(ctx, "obj") and ctx.obj:
                trigger_post_command_hooks(ctx)
    except Exception:
        # Silent failure - don't break CLI for tracking/suggestion issues
        pass


# Register all commands from modules
mcpt_cli.add_command(create_run_command())
mcpt_cli.add_command(create_list_command())
mcpt_cli.add_command(create_show_command())
mcpt_cli.add_command(create_create_group())
mcpt_cli.add_command(create_quickstart_group())
mcpt_cli.add_command(create_report_group())


if __name__ == "__main__":
    mcpt_main()
