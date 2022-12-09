"""
Rather than two knots, you now must simulate a rope consisting of ten knots. One knot is still the head of the rope and moves according to the series of motions. Each knot further down the rope follows the knot in front of it using the same rules as before.

Using the same series of motions as the above example, but with the knots marked H, 1, 2, ..., 9, the motions now occur as follows

Now, you need to keep track of the positions the new tail, 9, visits. In this example, the tail never moves, and so it only visits 1 position. However, be careful: more types of motion are possible than before, so you might want to visually compare your simulated rope to the one above.

Here's a larger example:

R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20

Now, the tail (9) visits 36 positions (including s) at least once:

Simulate your complete series of motions on a larger rope with ten knots. How many positions does the tail of the rope visit at least once?
"""

from typing import Literal

import numpy as np

Direction = Literal["R", "L", "U", "D"]


def update_head_position(
    head_position: tuple[int, int], direction: Direction
) -> tuple[int, int]:
    if direction == "R":
        return (head_position[0], head_position[1] + 1)
    elif direction == "L":
        return (head_position[0], head_position[1] - 1)
    elif direction == "U":
        return (head_position[0] - 1, head_position[1])
    else:
        return (head_position[0] + 1, head_position[1])


def update_tail_position(
    head_position: tuple[int, int], tail_position: tuple[int, int]
) -> tuple[int, int]:
    x_direction_diff = head_position[1] - tail_position[1]
    y_direction_diff = head_position[0] - tail_position[0]

    abs_x = abs(x_direction_diff)
    abs_y = abs(y_direction_diff)
    if abs_x < 2 and abs_y < 2:  # check if diagonal, adjacent or on top
        return tail_position
    elif abs_y == 0:  # horizontal move
        return tail_position[0], tail_position[1] + (x_direction_diff // 2)
    elif abs_x == 0:  # vertical move
        return tail_position[0] + (y_direction_diff // 2), tail_position[1]
    else:
        if x_direction_diff < 0:
            x_move = -1
        else:
            x_move = 1
        if y_direction_diff < 0:
            y_move = -1
        else:
            y_move = 1
        return tail_position[0] + y_move, tail_position[1] + x_move


def num_visited_positions_multi_knots(input_str: str) -> int:
    directions = [
        (direction, int(num))
        for direction, num in map(lambda line: line.split(), input_str.split("\n"))
    ]
    tail_visits = 1
    max_width = (sum(val for d, val in directions if d == "R") + 1) * 2
    max_height = (sum(val for d, val in directions if d == "U") + 1) * 2
    grid = np.zeros((max_height, max_width))
    grid[max_height // 2 - 1, max_width // 2] = 1
    knot_positions = [(max_height // 2 - 1, max_width // 2) for i in range(10)]
    for direction, val in directions:
        for step in range(val):
            head_position = update_head_position(knot_positions[0], direction)  # type: ignore
            knot_positions[0] = head_position
            for i, (knot_1, knot_2) in enumerate(
                zip(knot_positions, knot_positions[1:])
            ):
                knot_2 = update_tail_position(knot_1, knot_2)
                knot_positions[i + 1] = knot_2
            grid[knot_positions[-1]] = 1

    return grid.sum()
    return tail_visits


if __name__ == "__main__":
    input_str = open("data/day9.txt").read()

    print(num_visited_positions_multi_knots(input_str))
