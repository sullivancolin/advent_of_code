
from advent_of_code.day6.part1 import fish_after_interval


def test_fish_after_interfal() -> None:
    start_array = [3, 4, 3, 1, 2]
    assert fish_after_interval(start_array) == 5934
