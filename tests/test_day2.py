from advent_of_code.day2.part1 import input_mapping, strategy_total_score
from advent_of_code.day2.part2 import optimal_mapping, optimal_strategy_score

input = [
    ["A", "Y"],
    ["B", "X"],
    ["C", "Z"],
]


def test_strategy_total_score() -> None:

    move_input = [tuple(input_mapping[val] for val in row) for row in input]
    result = strategy_total_score(move_input)

    assert result == 15


def test_optimal_strategy_score() -> None:
    move_input = [(optimal_mapping[row[0]], row[1]) for row in input]
    result = optimal_strategy_score(move_input)
    assert result == 12
