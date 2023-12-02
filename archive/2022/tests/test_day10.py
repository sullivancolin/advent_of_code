from advent_of_code.day10.part1 import sum_interesting_signals
from advent_of_code.day10.part2 import print_screen


def test_sum_interesting_signals(day_10_test_input: str) -> None:
    result = sum_interesting_signals(day_10_test_input)
    assert result == 13140


def test_print_screen(day_10_test_input: str) -> None:
    result = print_screen(day_10_test_input)
    expected = """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######....."""
    assert result == expected
