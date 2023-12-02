from advent_of_code.day1.part1 import calculate_max_calories
from advent_of_code.day1.part2 import calculate_top_3_total_calories

toy_data = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""


def test_part1() -> None:
    result = calculate_max_calories(toy_data)
    assert result == 24000


def test_part2() -> None:
    result = calculate_top_3_total_calories(toy_data)
    assert result == 45000
