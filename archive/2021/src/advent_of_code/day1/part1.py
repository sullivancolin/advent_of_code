"""
To do this, count the number of times a depth measurement increases from the previous measurement. (There is no measurement before the first measurement.) In the example above, the changes are as follows:

199 (N/A - no previous measurement)
200 (increased)
208 (increased)
210 (increased)
200 (decreased)
207 (increased)
240 (increased)
269 (increased)
260 (decreased)
263 (increased)

In this example, there are 7 measurements that are larger than the previous measurement.
"""

# Original Answer before changing to work for part 1 and 2 at the same time
# def number_depth_increases(depths: list[int]) -> int:
#     pairs = zip(depths, depths[1:])
#     num_increased = 0
#     for first, second in pairs:
#         if second > first:
#             num_increased += 1
#     return num_increased


def number_depths_increased(depths: list[int], gap: int = 1) -> int:
    """Iterate over pairs of depths separated by interval `gap`,
    count number of times second depth is greater than first
    """
    pairs = zip(depths, depths[gap:])
    num_increased = 0
    for first, second in pairs:
        if second > first:
            num_increased += 1
    return num_increased


if __name__ == "__main__":
    with open("data/day1.txt") as infile:
        depths = [int(line.strip()) for line in infile]

    increased = number_depths_increased(depths)
    print(increased)
