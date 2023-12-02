"""
the submarine helpfully produces a list of nearby lines of vents (your puzzle input) for you to review. For example:

0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2

Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where x1,y1 are the coordinates of one end the line segment and x2,y2 are the coordinates of the other end. These line segments include the points at both ends. In other words:

    An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
    An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.

For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.

So, the horizontal and vertical lines from the above list would produce the following diagram:

.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111....

In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. Each position is shown as the number of lines which cover that point or . if no line covers that point. The top-left pair of 1s, for example, comes from 2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.

To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap. In the above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.

Consider only horizontal and vertical lines. At how many points do at least two lines overlap?
"""

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True, order=True)
class Point:
    x: int
    y: int

    @classmethod
    def from_str(cls, content: str):
        x, y = content.split(",")
        return cls(int(x), int(y))


def parse_file(filename: str) -> list[tuple[Point, Point]]:
    endpoints = []
    with open(filename) as infile:
        for line in infile:
            p1_str, p2_str = line.strip().split(" -> ")
            endpoints.append((Point.from_str(p1_str), Point.from_str(p2_str)))
    return endpoints


def get_shape(line_endpoints: list[tuple[Point, Point]]) -> tuple[int, int]:
    max_x = 0
    max_y = 0
    for segment in line_endpoints:
        for point in segment:
            if point.x > max_x:
                max_x = point.x
            if point.y > max_y:
                max_y = point.y
    return max_x + 1, max_y + 1


def update_grid(grid: np.ndarray, p1: Point, p2: Point) -> np.ndarray:
    if p1.x != p2.x and p1.y != p2.y:
        return grid
    if p1.x == p2.x:
        grid[p1.x, p1.y : p2.y + 1] += 1
    else:
        grid[p1.x : p2.x + 1, p1.y] += 1
    return grid


def get_number_overlaps(line_endpoints: list[tuple[Point, Point]]) -> int:
    shape = get_shape(line_endpoints)
    grid = np.zeros(shape)
    for p1, p2 in line_endpoints:
        if p2 < p1:
            grid = update_grid(grid, p2, p1)
        else:
            grid = update_grid(grid, p1, p2)

    return (grid > 1).sum()


if __name__ == "__main__":
    line_endpoints = parse_file("data/day5.txt")

    overlaps = get_number_overlaps(line_endpoints)
    print(overlaps)
