"""
The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup holder, and the ability to pick up and move multiple crates at once.

Again considering the example above, the crates begin in the same configuration:

    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

Moving a single crate from stack 2 to stack 1 behaves the same as before:

[D]
[N] [C]
[Z] [M] [P]
 1   2   3

However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates stay in the same order, resulting in this new configuration:

        [D]
        [N]
    [C] [Z]
    [M] [P]
 1   2   3

Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:

        [D]
        [N]
[C]     [Z]
[M]     [P]
 1   2   3

Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:

        [D]
        [N]
        [Z]
[M] [C] [P]
 1   2   3

In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.

Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to be ready to unload the final supplies. After the rearrangement procedure completes, what crate ends up on top of each stack?
"""

from collections import deque

from advent_of_code.day5.part1 import parse_moves, parse_stacks


def compute_efficient_end_state(
    stacks: list[deque[str]], moves: list[tuple[int, int, int]]
) -> str:
    for quantity, origin, destination in moves:
        crates = []
        for crate_num in range(quantity):
            crate = stacks[origin - 1].pop()
            crates.append(crate)
        for crate in crates[::-1]:
            stacks[destination - 1].append(crate)

    top_crates = [stack.pop() for stack in stacks]
    return "".join(top_crates)


def calculate_efficient_final_stacks(input_str: str) -> str:
    stacks_str, moves_str = input_str.split("\n\n")
    stacks = parse_stacks(stacks_str)
    moves = parse_moves(moves_str)
    end_state = compute_efficient_end_state(stacks, moves)
    return end_state


if __name__ == "__main__":
    input_str = open("data/day5.txt").read()

    final_state = calculate_efficient_final_stacks(input_str)

    print(final_state)
