"""
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2

In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top. Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a single crate, P.

Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:

[D]
[N] [C]
[Z] [M] [P]
 1   2   3

In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate to be moved (D) ends up below the second and third crates:

        [Z]
        [N]
    [C] [D]
    [M] [P]
 1   2   3

Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up below crate M:

        [Z]
        [N]
[M]     [D]
[C]     [P]
 1   2   3

Finally, one crate is moved from stack 1 to stack 2:

        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3

The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.

After the rearrangement procedure completes, what crate ends up on top of each stack?
"""
import re
from collections import deque

move_pattern = re.compile(r"(\d+)")


def split_stack_cols(line: str) -> list[str]:
    return [line[index] for index in range(1, len(line), 4)]


def parse_stacks(input_str: str) -> list[deque[str]]:
    stacks_col_strings, stack_ids = input_str.rsplit("\n", 1)
    stacks = [deque() for val in stack_ids.split()]
    for stack_col_line in stacks_col_strings.split("\n")[::-1]:
        for stack_id, crate_val in enumerate(split_stack_cols(stack_col_line)):
            if crate_val != " ":
                stacks[stack_id].append(crate_val)
    return stacks


def parse_moves(input_str: str) -> list[tuple[int, int, int]]:
    moves = []
    for line in input_str.split("\n"):
        nums = tuple(int(num) for num in move_pattern.findall(line))
        moves.append(nums)

    return moves


def compute_end_state(
    stacks: list[deque[str]], moves: list[tuple[int, int, int]]
) -> str:
    for quantity, origin, destination in moves:
        for crate_num in range(quantity):
            crate = stacks[origin - 1].pop()
            stacks[destination - 1].append(crate)

    top_crates = [stack.pop() for stack in stacks]
    return "".join(top_crates)


def calculate_final_stacks(input_str: str) -> str:
    stacks_str, moves_str = input_str.split("\n\n")
    stacks = parse_stacks(stacks_str)
    moves = parse_moves(moves_str)
    end_state = compute_end_state(stacks, moves)
    return end_state


if __name__ == "__main__":
    input_str = open("data/day5.txt").read()

    final_state = calculate_final_stacks(input_str)

    print(final_state)
