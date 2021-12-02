from advent_of_code.day1.part1 import number_depths_increased
from advent_of_code.day1.part2 import number_window_sum_increased


def test_number_increases() -> None:

    depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    num_increased = number_depths_increased(depths)

    assert num_increased == 7


def test_number_window_increases() -> None:
    """Test Part 2 with original implementation"""
    depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    number_increased = number_window_sum_increased(depths)

    assert number_increased == 5


def test_revised_number_window_increases() -> None:
    """Test Part 2 with revised implementation from Part 1"""
    depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    number_increased = number_depths_increased(depths, gap=3)

    assert number_increased == 5
