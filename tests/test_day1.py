from aoc.day1.part1 import calibration_sum
from aoc.day1.part2 import word_calibration_sum

input_text = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""


def test_day1_part1() -> None:
    """Test the sum of first and last calibration digits on the toy input."""
    assert calibration_sum(input_text) == 142


part2_input = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""


def test_day1_part2() -> None:
    """Test the sum of first and last calibration digits spelled as words on the toy input."""
    assert word_calibration_sum(part2_input) == 281
