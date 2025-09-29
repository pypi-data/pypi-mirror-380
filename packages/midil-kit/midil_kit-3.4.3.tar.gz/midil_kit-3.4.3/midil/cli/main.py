import click
from midil.cli.commands.init import init_command
from midil.cli.commands.launch import launch_command
from midil.cli.commands.version import version_command
from midil.cli.commands.test import test_command


@click.group()
def cli():
    """MIDIL CLI: Tools for project scaffolding, launching services, testing, and version info."""
    pass


cli.add_command(init_command)
cli.add_command(launch_command)
cli.add_command(version_command)
cli.add_command(test_command)
