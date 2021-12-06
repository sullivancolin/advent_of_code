"""
Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are chosen at random, and the chosen number is marked on all boards on which it appears. (Numbers may not appear on all boards.) If all numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)

The submarine has a bingo subsystem to help passengers (currently, you and the giant squid) pass the time. It automatically generates a random order in which to draw numbers and a random set of boards (your puzzle input). For example:

7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7

After the first five numbers are drawn (7, 4, 9, 5, and 11), there are no winners, but the boards are marked as follows (shown here adjacent to each other to save space):

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

After the next six numbers are drawn (17, 23, 2, 0, 14, and 21), there are still no winners:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

Finally, 24 is drawn:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

At this point, the third board wins because it has at least one complete row or column of marked numbers (in this case, the entire top row is marked: 14 21 17 24 4).

The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on that board; in this case, the sum is 188. Then, multiply that sum by the number that was just called when the board won, 24, to get the final score, 188 * 24 = 4512.

To guarantee victory against the giant squid, figure out which board will win first. What will your final score be if you choose that board?
"""
import numpy as np


def parse_file(filename: str) -> tuple[list[int], list[np.ndarray]]:
    boards = []
    with open(filename) as infile:
        numbers = [int(num) for num in infile.readline().strip().split(",")]
        while line := infile.readline():  # noqa
            rows = []
            for i in range(5):
                row = [int(num) for num in infile.readline().strip().split()]
                rows.append(row)
            boards.append(np.asarray(rows))
        return numbers, boards


def play_bingo(numbers: list[int], boards: list[np.ndarray]) -> int:
    board_shape = boards[0].shape
    board_states = [np.zeros(board_shape, dtype=bool) for board in boards]
    for num in numbers:
        for i, (board, state) in enumerate(zip(boards, board_states)):
            new_state = update_board_state(num, board, state)
            if is_bingo(new_state):
                board_sum = remain_sum(board, new_state)
                return board_sum * num
            board_states[i] = new_state
    raise ValueError("No Winning Board")


def remain_sum(board: np.ndarray, state: np.ndarray) -> int:
    return board[~state].sum()


def update_board_state(number: int, board: np.ndarray, state: np.ndarray) -> np.ndarray:
    num_is_in = board == number
    state = np.bitwise_or(num_is_in, state)
    return state


def check_rows(state_board: np.ndarray) -> np.bool_:
    return state_board.all(axis=1).any()


def check_columns(state_board: np.ndarray) -> np.bool_:
    return state_board.all(axis=0).any()


def is_bingo(state_board: np.ndarray) -> bool:
    if check_rows(state_board) or check_columns(state_board):
        return True
    return False


if __name__ == "__main__":
    numbers, boards = parse_file("data/day4.txt")
    print(play_bingo(numbers, boards))
