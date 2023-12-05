"""The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers.

Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. You exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

```
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
```

In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?
"""
from aoc.day3.part1 import Number, Part


def sum_gear_ratios(input_text: str) -> int:  # noqa C901
    """Get the sum of all the gear ratios.
        Traverse the grid to accumulate engine numbers and gears and making a lookup from coordinates to engine numbers.
        For each gear search the lookup for using it's position for valid engine numbers and if there are exactly 2 add them to a set. Return the sum.
    Args:
        input_text: Raw input string


    Returns:
        sum of all valid gear ratios"""

    parts = []
    coords = {}

    lines = input_text.splitlines()
    for i, line in enumerate(lines):
        num = ""
        cols = []
        for j, char in enumerate(line):
            if char.isdigit():
                num += char
                cols.append(j)
            elif char == "*":
                parts.append(Part(i, j))
                if num != "":
                    n = Number(int(num), i, cols)

                    for col in cols:
                        coords[(i, col)] = n
                    num = ""
                    cols = []
            else:
                if num != "":
                    n = Number(int(num), i, cols)

                    for col in cols:
                        coords[(i, col)] = n
                    num = ""
                    cols = []
        if num != "":
            n = Number(int(num), i, cols)
            for col in cols:
                coords[(i, col)] = n
            num = ""
            cols = []

    cum = 0
    for part in parts:
        possible_nums = set()
        for valid_coord in part.valid_coodinates():
            if valid_coord in coords:
                possible_nums.add(coords[valid_coord])
        if len(possible_nums) == 2:
            part1, part2 = tuple(possible_nums)
            cum += part1.value * part2.value

    return cum
