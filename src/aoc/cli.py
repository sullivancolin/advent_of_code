from importlib.metadata import version
from pathlib import Path

import typer
from rich import print

from aoc.day1.part1 import calibration_sum
from aoc.day1.part2 import word_calibration_sum
from aoc.day2.part1 import sum_valid_game_ids
from aoc.day2.part2 import sum_game_powers
from aoc.day3.part1 import sum_part_numbers
from aoc.day3.part2 import sum_gear_ratios
from aoc.day4.part1 import card_points
from aoc.day4.part2 import count_cards
from aoc.day5.part1 import nearest_location

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
    help="Command for running day1 stars",
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
    """Calculate the sum of all the first and last number words or digits on each line concatenated together."""
    with open(input_path) as infile:
        input_text = infile.read()
    total_sum = word_calibration_sum(input_text)
    print(
        f"The sum of the first and last calibration digits/words on each line is: [bold red]{total_sum}[/bold red]"
    )


cli.add_typer(day1app, name="day1")


day2app = typer.Typer(
    help="Command for running day2 stars",
    rich_markup_mode="rich",
)


@day2app.command(name="part1")
def day2part1(
    input_path: Path = typer.Argument(
        Path("data/day2.txt"), help="Path to file containing the input"
    ),
) -> None:
    """Calculate the sum of all Game IDs"""
    with open(input_path) as infile:
        input_text = infile.read()
    total_sum = sum_valid_game_ids(input_text)
    print(f"The sum of the valid game IDs is: [bold red]{total_sum}[/bold red]")


@day2app.command(name="part2")
def day2part2(
    input_path: Path = typer.Argument(
        Path("data/day2.txt"), help="Path to file containing the input"
    ),
) -> None:
    """Calculate the sum of all Game Powers"""
    with open(input_path) as infile:
        input_text = infile.read()
    total_sum = sum_game_powers(input_text)
    print(f"The sum of the game powers is: [bold red]{total_sum}[/bold red]")


cli.add_typer(day2app, name="day2")

day3app = typer.Typer(
    help="Command for running day3 stars",
    rich_markup_mode="rich",
)


@day3app.command(name="part1")
def day3part1(
    input_path: Path = typer.Argument(
        Path("data/day3.txt"), help="Path to file containing the input"
    ),
) -> None:
    """Calculate the sum of engine parts."""
    with open(input_path) as infile:
        input_text = infile.read()
    total_sum = sum_part_numbers(input_text)
    print(f"The sum of the engine parts is: [bold red]{total_sum}[/bold red]")


@day3app.command(name="part2")
def day3part2(
    input_path: Path = typer.Argument(
        Path("data/day3.txt"), help="Path to file containing the input"
    ),
) -> None:
    """Calculate the sum of all gears"""
    with open(input_path) as infile:
        input_text = infile.read()
    total_sum = sum_gear_ratios(input_text)
    print(f"The sum of the gear ratios is: [bold red]{total_sum}[/bold red]")


cli.add_typer(day3app, name="day3")

day4app = typer.Typer(
    help="Command for running day4 stars",
    rich_markup_mode="rich",
)


day4app = typer.Typer(
    help="Command for running day4 stars",
    rich_markup_mode="rich",
)


@day4app.command(name="part1")
def day4part1(
    input_path: Path = typer.Argument(
        Path("data/day4.txt"), help="Path to file containing the input"
    ),
) -> None:
    """Calculate the sum of all the scratch card scores"""
    with open(input_path) as infile:
        input_text = infile.read()
    total_sum = card_points(input_text)
    print(f"The sum of card scores is: [bold red]{total_sum}[/bold red]")


@day4app.command(name="part2")
def day4part2(
    input_path: Path = typer.Argument(
        Path("data/day4.txt"), help="Path to file containing the input"
    ),
) -> None:
    """Count the total number of scratch cards"""
    with open(input_path) as infile:
        input_text = infile.read()
    total_sum = count_cards(input_text)
    print(f"The final number of scratch cards is: [bold red]{total_sum}[/bold red]")


cli.add_typer(day4app, name="day4")

day5app = typer.Typer(
    help="Command for running day5 stars",
    rich_markup_mode="rich",
)


@day5app.command(name="part1")
def day5part1(
    input_path: Path = typer.Argument(
        Path("data/day5.txt"), help="Path to file containing the input"
    ),
) -> None:
    """Calculate the nearest location for planting."""
    with open(input_path) as infile:
        input_text = infile.read()
    total_sum = nearest_location(input_text)
    print(f"The nearest location is: [bold red]{total_sum}[/bold red]")


cli.add_typer(day5app, name="day5")
