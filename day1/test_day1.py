from .day1_part1 import number_depth_increases
from .day1_part2 import number_window_sum_increased


def test_number_increases() -> None:

    depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    num_increased = number_depth_increases(depths)

    assert num_increased == 7


def test_number_window_increases() -> None:
    depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    number_increased = number_window_sum_increased(depths)

    assert number_increased == 5
