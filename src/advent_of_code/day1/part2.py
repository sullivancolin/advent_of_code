"""
Instead, consider sums of a three-measurement sliding window. Again considering the above example:

199  A
200  A B
208  A B C
210    B C D
200  E   C D
207  E F   D
240  E F G
269    F G H
260      G H
263        H

Start by comparing the first and second three-measurement windows. The measurements in the first window are marked A (199, 200, 208); their sum is 199 + 200 + 208 = 607. The second window is marked B (200, 208, 210); its sum is 618. The sum of measurements in the second window is larger than the sum of the first, so this first comparison increased.

Your goal now is to count the number of times the sum of measurements in this sliding window increases from the previous sum. So, compare A with B, then compare B with C, then C with D, and so on. Stop when there aren't enough measurements left to create a new three-measurement sum.

In the above example, the sum of each three-measurement window is as follows:

A: 607 (N/A - no previous sum)
B: 618 (increased)
C: 618 (no change)
D: 617 (decreased)
E: 647 (increased)
F: 716 (increased)
G: 769 (increased)
H: 792 (increased)

In this example, there are 5 sums that are larger than the previous sum.

Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?
"""

from .part1 import number_depths_increased


# Original Anwser
def number_window_sum_increased(depths: list[int]) -> int:
    number_increased = 0
    triples = zip(depths, depths[1:], depths[2:])
    triple_sums = [sum(triple) for triple in triples]
    sum_pairs = zip(triple_sums, triple_sums[1:])
    for first, second in sum_pairs:
        if second > first:
            number_increased += 1
    return number_increased


if __name__ == "__main__":
    with open("data/day1.txt") as infile:
        depths = [int(line.strip()) for line in infile]

    increased = number_depths_increased(depths, gap=4)
    print(increased)
