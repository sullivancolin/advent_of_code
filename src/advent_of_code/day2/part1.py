"""
Now, you need to figure out how to pilot this thing.

It seems like the submarine can take a series of commands like forward 1, down 2, or up 3:

    forward X increases the horizontal position by X units.
    down X increases the depth by X units.
    up X decreases the depth by X units.

Note that since you're on a submarine, down and up affect your depth, and so they have the opposite result of what you might expect.

The submarine seems to already have a planned course (your puzzle input). You should probably figure out where it's going. For example:

forward 5
down 5
forward 8
up 3
down 8
forward 2

Your horizontal position and depth both start at 0. The steps above would then modify them as follows:

    forward 5 adds 5 to your horizontal position, a total of 5.
    down 5 adds 5 to your depth, resulting in a value of 5.
    forward 8 adds 8 to your horizontal position, a total of 13.
    up 3 decreases your depth by 3, resulting in a value of 2.
    down 8 adds 8 to your depth, resulting in a value of 10.
    forward 2 adds 2 to your horizontal position, a total of 15.

After following these instructions, you would have a horizontal position of 15 and a depth of 10. (Multiplying these together produces 150.)

Calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth?
"""


def parse_file(filename: str) -> list[tuple[str, int]]:
    def process_line(line: str) -> tuple[str, int]:
        tup = line.strip().split()
        return tup[0], int(tup[1])

    with open(filename) as infile:
        directions = [process_line(line) for line in infile]
    return directions


def get_positions(directions: list[tuple[str, int]]) -> tuple[int, int]:
    horizontal = 0
    vertical = 0

    for direction, distance in directions:
        if direction == "forward":
            horizontal += distance
        else:
            if direction == "up":
                distance = -1 * distance
            vertical += distance
    return vertical, horizontal


def get_distance_product(directions: list[tuple[str, int]]) -> int:
    vertical, horizonal = get_positions(directions)
    return vertical * horizonal


if __name__ == "__main__":
    directions = parse_file("data/day2.txt")
    print(get_distance_product(directions))
