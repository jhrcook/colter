"""Command line interface."""

from typer import Typer

app = Typer(add_completion=False)


@app.command()
def main() -> None:
    print("Hello from colter!")
