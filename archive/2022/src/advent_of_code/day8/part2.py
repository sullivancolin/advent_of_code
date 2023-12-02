"""
To measure the viewing distance from a given tree, look up, down, left, and right from that tree; stop if you reach an edge or at the first tree that is the same height or taller than the tree under consideration. (If a tree is right on the edge, at least one of its viewing distances will be zero.)

The Elves don't care about distant trees taller than those found by the rules above; the proposed tree house has large eaves to keep it dry, so they wouldn't be able to see higher than the tree house anyway.

In the example above, consider the middle 5 in the second row:

30373
25512
65332
33549
35390

    Looking up, its view is not blocked; it can see 1 tree (of height 3).
    Looking left, its view is blocked immediately; it can see only 1 tree (of height 5, right next to it).
    Looking right, its view is not blocked; it can see 2 trees.
    Looking down, its view is blocked eventually; it can see 2 trees (one of height 3, then the tree of height 5 that blocks its view).

A tree's scenic score is found by multiplying together its viewing distance in each of the four directions. For this tree, this is 4 (found by multiplying 1 * 1 * 2 * 2).

However, you can do even better: consider the tree of height 5 in the middle of the fourth row:

30373
25512
65332
33549
35390

    Looking up, its view is blocked at 2 trees (by another tree with a height of 5).
    Looking left, its view is not blocked; it can see 2 trees.
    Looking down, its view is also not blocked; it can see 1 tree.
    Looking right, its view is blocked at 2 trees (by a massive tree of height 9).

This tree's scenic score is 8 (2 * 2 * 1 * 2); this is the ideal spot for the tree house.

Consider each tree on your map. What is the highest scenic score possible for any tree?
"""


def view_score(tree: int, view: list[int]) -> int:
    score = 0
    for neighbor in view:
        score += 1
        if tree <= neighbor:
            break
    return score


def best_scenic_score(input_str: str) -> int:
    grid_as_rows = [[int(char) for char in line] for line in input_str.split("\n")]

    grid_as_columns = [list(i) for i in zip(*grid_as_rows)]

    best_score = 0
    for i, row in enumerate(grid_as_rows):
        for j, col in enumerate(row):
            left_score = view_score(col, row[:j][::-1])
            right_score = view_score(col, row[j + 1 :])
            top_score = view_score(col, grid_as_columns[j][:i][::-1])
            bottom_score = view_score(col, grid_as_columns[j][i + 1 :])
            score = left_score * right_score * top_score * bottom_score
            if score > best_score:
                best_score = score
    return best_score


if __name__ == "__main__":
    input_str = open("data/day8.txt").read()

    print(best_scenic_score(input_str))
