from advent_of_code.day9.part1 import num_visited_positions
from advent_of_code.day9.part2 import num_visited_positions_multi_knots

input_str = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""


def test_num_visited_positions() -> None:
    result = num_visited_positions(input_str)
    assert result == 13


new_input = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""


def test_num_multi_knot() -> None:
    result = num_visited_positions_multi_knots(new_input)
    assert result == 36
