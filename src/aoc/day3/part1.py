"""
# Day 3: Gear Ratios

You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

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

In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?

"""
from collections.abc import Iterable
from dataclasses import dataclass


@dataclass
class Number:
    """Dataclass for containing a number and it's position"""

    value: int
    row: int
    columns: list[int]

    def __hash__(self) -> int:
        """The hash of a Number is its position. Used for making it possible to use as a key in a dictionary"""
        return hash(f"{self.row}, {self.columns}")


@dataclass
class Part:
    """Dataclass for storing the position of a engine number"""

    row: int
    column: int

    def valid_coodinates(self) -> Iterable[tuple[int, int]]:
        """Get an iterable of valid positions for engine numbers

        Returns:
            A generator of position tuples for valid engine numbers
        """
        for j in range(self.column - 1, self.column + 2):
            for i in range(self.row - 1, self.row + 2):
                yield (i, j)


def sum_part_numbers(input_text: str) -> int:  # noqa C901
    """Get the sum of all the valid engine numbers that are adjacent or diagonal to a engine part.
        Traverse the grid to accumulate engine numbers and parts and making a lookup from coordinates to engine numbers.
        For each part search the lookup for using it's position for valid engine numbers and at them to the set. Return the sum.
    Args:
        input_text: Raw input string


    Returns:
        sum of all valid engine numbers
    """

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
            elif char != ".":
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

    valid_parts = set()
    for part in parts:
        for valid_coord in part.valid_coodinates():
            if valid_coord in coords:
                valid_parts.add(coords[valid_coord])

    return sum(part.value for part in valid_parts)
