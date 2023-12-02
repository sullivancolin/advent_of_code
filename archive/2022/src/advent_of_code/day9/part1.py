"""
Then, by following a hypothetical series of motions (your puzzle input) for the head, you can determine how the tail will move.

Due to the aforementioned Planck lengths, the rope must be quite short; in fact, the head (H) and tail (T) must always be touching (diagonally adjacent and even overlapping both count as touching):

....
.TH.
....

....
.H..
..T.
....

...
.H. (H covers T)
...

If the head is ever two steps directly up, down, left, or right from the tail, the tail must also move one step in that direction so it remains close enough:

Otherwise, if the head and tail aren't touching and aren't in the same row or column, the tail always moves one step diagonally to keep up:

You just need to work out where the tail goes as the head follows a series of motions. Assume the head and the tail both start at the same position, overlapping.

For example:
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2

This series of motions moves the head right four steps, then up four steps, then left three steps, then down one step, and so on. After each step, you'll need to update the position of the tail if the step means the head is no longer adjacent to the tail. Visually, these motions occur as follows (s marks the starting position as a reference point):

After simulating the rope, you can count up all of the positions the tail visited at least once. In this diagram, s again marks the starting position (which the tail also visited) and # marks other positions the tail visited:

..##..
...##.
.####.
....#.
s###..

So, there are 13 positions the tail visited at least once.

Simulate your complete hypothetical series of motions. How many positions does the tail of the rope visit at least once?
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


def num_visited_positions(input_str: str) -> int:
    directions = [
        (direction, int(num))
        for direction, num in map(lambda line: line.split(), input_str.split("\n"))
    ]
    tail_visits = 1
    max_width = (sum(val for d, val in directions if d == "R") + 1) * 2
    max_height = (sum(val for d, val in directions if d == "U") + 1) * 2
    grid = np.zeros((max_height, max_width))
    grid[max_height // 2 - 1, max_width // 2] = 1
    head_position = (max_height // 2 - 1, max_width // 2)
    tail_position = head_position
    for direction, val in directions:
        for step in range(val):
            head_position = update_head_position(head_position, direction)  # type: ignore
            tail_position = update_tail_position(head_position, tail_position)
            grid[tail_position] = 1

    return grid.sum()
    return tail_visits


if __name__ == "__main__":
    input_str = open("data/day9.txt").read()

    print(num_visited_positions(input_str))
