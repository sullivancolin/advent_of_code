from advent_of_code.day4.part1 import total_overlaps
from advent_of_code.day4.part2 import total_any_overlaps

input_str = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""


def test_total_overlaps() -> None:
    result = total_overlaps(input_str)
    assert result == 2


def test_any_total_overlaps() -> None:
    result = total_any_overlaps(input_str)
    assert result == 4
