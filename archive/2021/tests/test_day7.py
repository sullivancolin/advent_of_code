import sys

from advent_of_code.day7.part1 import get_least_fuel
from advent_of_code.day7.part2 import get_actual_least_fuel, triangular_number

sys.setrecursionlimit(10 ** 6)


positions = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


def test_get_least_fuel() -> None:
    assert get_least_fuel(positions) == 37


def test_triangular_number() -> None:
    assert triangular_number(4) == 10


def test_get_actual_least_fuel() -> None:
    assert get_actual_least_fuel(positions) == 168
