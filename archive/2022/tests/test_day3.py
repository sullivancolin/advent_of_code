from advent_of_code.day3.part1 import total_priorities
from advent_of_code.day3.part2 import total_group_priorities

input_string = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""


def test_total_priorities() -> None:
    result = total_priorities(input_string)
    assert result == 157


def test_total_group_priorities() -> None:
    result = total_group_priorities(input_string)
    assert result == 70
