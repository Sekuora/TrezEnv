import click
from cli_commands import setup
from primals import __all__

@click.group()
@click.version_option(version='1.1.0')
def cli() -> None:
    print("Trezenv has been found in your system!")


cli.add_command(setup.set)

cli.add_command(setup.check)

cli.add_command(setup.init)

if __name__ == "__main__":
    try:
        cli()
    except Exception as e:
        print(f"Error: {e}")