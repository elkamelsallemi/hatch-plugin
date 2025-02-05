# SPDX-FileCopyrightText: 2025-present elkamelsallemi <elkamel.sallemi@gmail.com>
#
# SPDX-License-Identifier: MIT
import click
import subprocess
from hatch_plugin.__about__ import __version__


@click.group(context_settings={"help_option_names": ["-h", "--help"]}, invoke_without_command=True)
@click.version_option(version=__version__, prog_name="monorepo")
def monorepo():
    """Build the project using Hatch."""
    result = subprocess.run(['hatch', 'build'], capture_output=True, text=True)
    if result.returncode == 0:
        click.echo("Build successful.")
    else:
        click.echo(f"Build failed with error: {result.stderr}")
        exit(result.returncode)