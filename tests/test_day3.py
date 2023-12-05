from aoc.day3.part1 import sum_part_numbers
from aoc.day3.part2 import sum_gear_ratios

input_text = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


def test_sum_part_numbers() -> None:
    assert sum_part_numbers(input_text) == 4361


def test_sum_gear_ratios() -> None:
    assert sum_gear_ratios(input_text) == 467835
