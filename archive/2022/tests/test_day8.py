from advent_of_code.day8.part1 import num_visible_trees
from advent_of_code.day8.part2 import best_scenic_score

input_str = """30373
25512
65332
33549
35390"""


def test_num_visible_trees() -> None:
    result = num_visible_trees(input_str)
    assert result == 21


def test_best_scenic_score() -> None:
    result = best_scenic_score(input_str)
    assert result == 8
