# -*- coding: utf-8 -*-

"""Console script for docker_kernel_provider."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for docker_kernel_provider."""
    click.echo("Replace this message by putting your code into "
               "docker_kernel_provider.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
