from importlib.metadata import version
from pathlib import Path

import typer
from rich import print

from aoc.day1.part1 import calibration_sum
from aoc.day1.part2 import word_calibration_sum

__version__ = version(__package__)


def version_info() -> str:
    """Helpful environment information for reproducible bug reports.

    Returns:
        str: Nicely formatted environment info.
    """
    import platform
    import sys
    from pathlib import Path

    info = {
        "aoc version": __version__,
        "install path": Path(__file__).resolve().parent,
        "python version": sys.version,
        "platform": platform.platform(),
    }
    return "\n".join(
        "{:>30} {}".format(k + ":", str(v).replace("\n", " ")) for k, v in info.items()
    )


##########################################################################
# CLI command and subcommands                                            #
#                                                                        #
#                                                                        #
##########################################################################

cli = typer.Typer(
    help="CLI interface for `aoc` package.",
    rich_markup_mode="rich",
)


def version_callback(value: bool) -> None:
    if value:
        print(f"{__version__}")
        raise typer.Exit()


@cli.callback()
def main(
    version: bool = typer.Option(
        None,
        "--version",
        "-v",
        help="Print the current version.",
        callback=version_callback,
        is_eager=True,
    ),
) -> None:
    return


@cli.command()
def debug_version_info() -> None:
    """Print debug information to terminal."""
    typer.echo(version_info())


day1app = typer.Typer(
    help="command for running day1 stars",
    rich_markup_mode="rich",
)


@day1app.command(name="part1")
def day1part1(
    input_path: Path = typer.Argument(
        Path("data/day1.txt"), help="Path to file containing the input"
    ),
) -> None:
    """Calculate the sum of all the first and last digits on each line concatenated together."""
    with open(input_path) as infile:
        input_text = infile.read()
    total_sum = calibration_sum(input_text)
    print(
        f"The sum of the first and last calibration digits on each line is: [bold red]{total_sum}[/bold red]"
    )


@day1app.command(name="part2")
def day1part2(
    input_path: Path = typer.Argument(
        Path("data/day1.txt"), help="Path to file containing the input"
    ),
) -> None:
    with open(input_path) as infile:
        input_text = infile.read()
    total_sum = word_calibration_sum(input_text)
    print(
        f"The sum of the first and last calibration digits/words on each line is: [bold red]{total_sum}[/bold red]"
    )


cli.add_typer(day1app, name="day1")
