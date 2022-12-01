"""
figure out which board will win last and choose that one. That way, no matter which boards it picks, it will win for sure.

In the above example, the second board is the last to win, which happens after 13 is eventually called and its middle column is completely marked. If you were to keep playing until this point, the second board would have a sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

Figure out which board will win last. Once it wins, what would its final score be?
"""
import numpy as np

from .part1 import is_bingo, parse_file, remain_sum, update_board_state


def all_winners(board_states: list[np.ndarray]) -> bool:
    return all(is_bingo(state) for state in board_states)


def lose_bingo(numbers: list[int], boards: list[np.ndarray]) -> int:
    board_shape = boards[0].shape
    board_states = [np.zeros(board_shape, dtype=bool) for board in boards]
    for num in numbers:
        for i, (board, state) in enumerate(zip(boards, board_states)):
            new_state = update_board_state(num, board, state)
            board_states[i] = new_state
            if all_winners(board_states):
                remaining = remain_sum(board, new_state)
                return remaining * num
    raise ValueError("No Winning Board")


if __name__ == "__main__":
    numbers, boards = parse_file("data/day4.txt")
    print(lose_bingo(numbers, boards))
