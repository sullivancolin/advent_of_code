import pytest

from advent_of_code.day3.part1 import get_pressure
from advent_of_code.day3.part2 import get_life_support


@pytest.fixture
def diagnostics() -> list[list[int]]:
    input = """00100
    11110
    10110
    10111
    10101
    01111
    00111
    11100
    10000
    11001
    00010
    01010"""

    diagnostics = [list(map(int, list(line.strip()))) for line in input.split("\n")]
    return diagnostics


def test_pressure(diagnostics) -> None:
    assert get_pressure(diagnostics) == 198


def test_life_support(diagnostics) -> None:
    assert get_life_support(diagnostics) == 230
