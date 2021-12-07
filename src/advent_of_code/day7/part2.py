"""
As it turns out, crab submarine engines don't burn fuel at a constant rate. Instead, each change of 1 step in horizontal position costs 1 more unit of fuel than the last: the first step costs 1, the second step costs 2, the third step costs 3, and so on.

As each crab moves, moving further becomes more expensive. This changes the best horizontal position to align them all on; in the example above, this becomes 5:

    Move from 16 to 5: 66 fuel
    Move from 1 to 5: 10 fuel
    Move from 2 to 5: 6 fuel
    Move from 0 to 5: 15 fuel
    Move from 4 to 5: 1 fuel
    Move from 2 to 5: 6 fuel
    Move from 7 to 5: 3 fuel
    Move from 1 to 5: 10 fuel
    Move from 2 to 5: 6 fuel
    Move from 14 to 5: 45 fuel

This costs a total of 168 fuel. This is the new cheapest possible outcome; the old alignment position (2) now costs 206 fuel instead.

Determine the horizontal position that the crabs can align to using the least fuel possible so they can make you an escape route! How much fuel must they spend to align to that position?
"""
import sys
from functools import cache

import numpy as np

from .part1 import parse_file

sys.setrecursionlimit(10 ** 6)


@cache
def triangular_number(n):
    if n == 0:
        return n
    return n + triangular_number(n - 1)


def get_actual_costs_for_position(position: int, max_position: int) -> list[int]:
    return [
        triangular_number(abs(x)) for x in range(position, position - max_position, -1)
    ]


def get_actual_least_fuel(positions: list[int]) -> int:
    max_position = max(positions) + 1
    grid = np.asarray(
        [
            get_actual_costs_for_position(position, max_position)
            for position in positions
        ]
    )

    fuel_costs = grid.sum(axis=0)
    return fuel_costs.min()


if __name__ == "__main__":
    positions = parse_file("data/day7.txt")

    print(get_actual_least_fuel(positions))
