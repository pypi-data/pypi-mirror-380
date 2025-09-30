#!/usr/bin/env python3
"""
Merobox CLI
A Python CLI tool for managing Calimero nodes in Docker containers.
"""

import click

from merobox.commands import (
    bootstrap,
    call,
    health,
    identity,
    install,
    join,
    list,
    logs,
    nuke,
    run,
    stop,
)

from . import __version__


@click.group()
@click.version_option(version=__version__)
def cli():
    """Merobox CLI - Manage Calimero nodes in Docker containers."""
    pass


# Add commands to the CLI group
cli.add_command(run)
cli.add_command(stop)
cli.add_command(list)
cli.add_command(logs)
cli.add_command(health)
cli.add_command(install)
cli.add_command(nuke)
cli.add_command(identity)
cli.add_command(join)
cli.add_command(call)
cli.add_command(bootstrap)

if __name__ == "__main__":
    cli()
