"""
Crab submarines have limited fuel, so you need to find a way to make all of their horizontal positions match while requiring them to spend as little fuel as possible.

For example, consider the following horizontal positions:

16,1,2,0,4,2,7,1,2,14

This means there's a crab with horizontal position 16, a crab with horizontal position 1, and so on.

Each change of 1 step in horizontal position of a single crab costs 1 fuel. You could choose any horizontal position to align them all on, but the one that costs the least fuel is horizontal position 2:

    Move from 16 to 2: 14 fuel
    Move from 1 to 2: 1 fuel
    Move from 2 to 2: 0 fuel
    Move from 0 to 2: 2 fuel
    Move from 4 to 2: 2 fuel
    Move from 2 to 2: 0 fuel
    Move from 7 to 2: 5 fuel
    Move from 1 to 2: 1 fuel
    Move from 2 to 2: 0 fuel
    Move from 14 to 2: 12 fuel

This costs a total of 37 fuel. This is the cheapest possible outcome; more expensive outcomes include aligning at position 1 (41 fuel), position 3 (39 fuel), or position 10 (71 fuel).

Determine the horizontal position that the crabs can align to using the least fuel possible. How much fuel must they spend to align to that position?
"""

import numpy as np


def parse_file(filename: str):
    with open(filename) as infile:
        return [int(x) for x in infile.read().strip().split(",")]


def get_costs_for_position(position: int, max_position: int) -> list[int]:
    return [abs(x) for x in range(position, position - max_position, -1)]


def get_least_fuel(positions: list[int]) -> int:
    max_position = max(positions) + 1
    grid = np.asarray(
        [get_costs_for_position(position, max_position) for position in positions]
    )

    fuel_costs = grid.sum(axis=0)
    return fuel_costs.min()


if __name__ == "__main__":
    positions = parse_file("data/day7.txt")

    print(get_least_fuel(positions))
