import click

@click.command()
def compose_command() -> None:
    """chain-compose"""
    click.echo("Hello from chain-compose!")

if __name__ == "__main__":
    compose_command()
