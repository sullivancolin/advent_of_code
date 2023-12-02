"""
It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like to know the number of pairs that overlap at all.

In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:

    5-7,7-9 overlaps in a single section, 7.
    2-8,3-7 overlaps all of the sections 3 through 7.
    6-6,4-6 overlaps in a single section, 6.
    2-6,4-8 overlaps in sections 4, 5, and 6.

So, in this example, the number of overlapping assignment pairs is 4.

In how many assignment pairs do the ranges overlap?
"""
from advent_of_code.day4.part1 import make_range_tup


def total_any_overlaps(input_string: str) -> int:
    total = 0
    for line in input_string.split("\n"):
        range1_str, range2_str = line.split(",")
        start1, end1 = make_range_tup(range1_str)
        start2, end2 = make_range_tup(range2_str)
        if start1 >= start2 and start1 <= end2:
            total += 1
        elif start1 <= start2 and end1 >= start2:
            total += 1
    return total


if __name__ == "__main__":
    input_string = open("data/day4.txt").read()

    overlaps = total_any_overlaps(input_string)

    print(overlaps)
