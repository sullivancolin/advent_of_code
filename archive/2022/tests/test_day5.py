from advent_of_code.day5.part1 import calculate_final_stacks
from advent_of_code.day5.part2 import calculate_efficient_final_stacks

input_str = """    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


def test_calculate_final_stacks() -> None:
    result = calculate_final_stacks(input_str)
    assert result == "CMZ"


def test_calculate_efficient_final_stacks() -> None:
    result = calculate_efficient_final_stacks(input_str)
    assert result == "MCD"
