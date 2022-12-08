"""
First, determine whether there is enough tree cover here to keep a tree house hidden. To do this, you need to count the number of trees that are visible from outside the grid when looking directly along a row or column.

The Elves have already launched a quadcopter to generate a map with the height of each tree (your puzzle input). For example:

30373
25512
65332
33549
35390

Each tree is represented as a single digit whose value is its height, where 0 is the shortest and 9 is the tallest.

A tree is visible if all of the other trees between it and an edge of the grid are shorter than it. Only consider trees in the same row or column; that is, only look up, down, left, or right from any given tree.

All of the trees around the edge of the grid are visible - since they are already on the edge, there are no trees to block the view. In this example, that only leaves the interior nine trees to consider:

    The top-left 5 is visible from the left and top. (It isn't visible from the right or bottom since other trees of height 5 are in the way.)
    The top-middle 5 is visible from the top and right.
    The top-right 1 is not visible from any direction; for it to be visible, there would need to only be trees of height 0 between it and an edge.
    The left-middle 5 is visible, but only from the right.
    The center 3 is not visible from any direction; for it to be visible, there would need to be only trees of at most height 2 between it and an edge.
    The right-middle 3 is visible from the right.
    In the bottom row, the middle 5 is visible, but the 3 and 4 are not.

With 16 trees visible on the edge and another 5 visible in the interior, a total of 21 trees are visible in this arrangement.

Consider your map; how many trees are visible from outside the grid?
"""


def visible(tree, row: list[int]) -> bool:
    if all(val < tree for val in row):
        return True
    return False


from_left = visible
from_right = visible
from_top = visible
from_bottom = from_right


def num_visible_trees(input_str: str) -> int:
    grid_as_rows = [[int(char) for char in line] for line in input_str.split("\n")]

    grid_as_columns = [list(i) for i in zip(*grid_as_rows)]

    base_visible = len(grid_as_rows) * 2 + (len(grid_as_columns) - 2) * 2

    for i, row in enumerate(grid_as_rows[1:-1]):
        for j, col in enumerate(row[1:-1]):
            if from_left(col, row[: j + 1]):
                base_visible += 1
                continue
            if from_right(col, row[j + 2 :]):
                base_visible += 1
                continue
            if from_top(col, grid_as_columns[j + 1][: i + 1]):
                base_visible += 1
                continue
            if from_bottom(col, grid_as_columns[j + 1][i + 2 :]):
                base_visible += 1
                continue

    return base_visible


if __name__ == "__main__":
    input_str = open("data/day8.txt").read()

    print(num_visible_trees(input_str))
