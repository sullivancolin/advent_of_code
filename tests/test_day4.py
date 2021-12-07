import numpy as np
import pytest

from advent_of_code.day4.part1 import (check_columns, check_rows, play_bingo,
                                       remain_sum, update_board_state)
from advent_of_code.day4.part2 import lose_bingo

state_boards = [
    np.asarray([[True, False, False], [False, True, False], [False, False, True]]),
    np.asarray([[True, True, True], [False, True, False], [False, False, True]]),
    np.asarray([[True, False, True], [False, True, True], [False, False, True]]),
]

sample_board = np.arange(9).reshape(3, 3)


row_expected = [False, True, False]
col_expected = [False, False, True]


def test_update_state():
    state = np.zeros((3, 3), dtype=bool)
    for num in range(3):
        state = update_board_state(num, sample_board, state)
        assert state.sum() == num + 1
    assert np.all(np.equal(state[0, :], np.ones((3,), dtype=bool)))
    assert np.all(np.equal(state[1:, :], np.zeros((2, 3), dtype=bool)))


@pytest.mark.parametrize("board,expected", zip(state_boards, row_expected))
def test_check_rows(board: np.ndarray, expected: bool) -> None:
    assert check_rows(board) == expected


@pytest.mark.parametrize("board,expected", zip(state_boards, col_expected))
def test_check_columns(board: np.ndarray, expected: bool) -> None:
    assert check_columns(board) == expected


def test_unmarked_sum() -> None:
    state = np.asarray(
        [[False, True, False], [False, True, False], [False, True, False]]
    )
    remaining = remain_sum(sample_board, state)
    assert remaining == 24


numbers = [
    7,
    4,
    9,
    5,
    11,
    17,
    23,
    2,
    0,
    14,
    21,
    24,
    10,
    16,
    13,
    6,
    15,
    25,
    12,
    22,
    18,
    20,
    8,
    19,
    3,
    26,
    1,
]

boards = [
    np.asarray(
        [
            [22, 13, 17, 11, 0],
            [8, 2, 23, 4, 24],
            [21, 9, 14, 16, 7],
            [6, 10, 3, 18, 5],
            [1, 12, 20, 15, 19],
        ]
    ),
    np.asarray(
        [
            [3, 15, 0, 2, 22],
            [9, 18, 13, 17, 5],
            [19, 8, 7, 25, 23],
            [20, 11, 10, 24, 4],
            [14, 21, 16, 12, 6],
        ]
    ),
    np.asarray(
        [
            [14, 21, 17, 24, 4],
            [10, 16, 15, 9, 19],
            [18, 8, 23, 26, 20],
            [22, 11, 13, 6, 5],
            [2, 0, 12, 3, 7],
        ]
    ),
]


def test_play_bingo() -> None:
    assert play_bingo(numbers, boards) == 4512


def test_lose_bingo() -> None:
    assert lose_bingo(numbers, boards) == 1924
