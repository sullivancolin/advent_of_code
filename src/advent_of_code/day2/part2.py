"""
In addition to horizontal position and depth, you'll also need to track a third value, aim, which also starts at 0. The commands also mean something entirely different than you first thought:

    down X increases your aim by X units.
    up X decreases your aim by X units.
    forward X does two things:
        It increases your horizontal position by X units.
        It increases your depth by your aim multiplied by X.

Again note that since you're on a submarine, down and up do the opposite of what you might expect: "down" means aiming in the positive direction.

Now, the above example does something different:

    forward 5 adds 5 to your horizontal position, a total of 5. Because your aim is 0, your depth does not change.
    down 5 adds 5 to your aim, resulting in a value of 5.
    forward 8 adds 8 to your horizontal position, a total of 13. Because your aim is 5, your depth increases by 8*5=40.
    up 3 decreases your aim by 3, resulting in a value of 2.
    down 8 adds 8 to your aim, resulting in a value of 10.
    forward 2 adds 2 to your horizontal position, a total of 15. Because your aim is 10, your depth increases by 2*10=20 to a total of 60.

After following these new instructions, you would have a horizontal position of 15 and a depth of 60. (Multiplying these produces 900.)

Using this new interpretation of the commands, calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth?
"""

from .part1 import parse_file


def get_aimed_positions(directions: list[tuple[str, int]]) -> tuple[int, int]:
    horizontal = 0
    vertical = 0
    aim = 0

    for direction, amount in directions:
        if direction == "forward":
            horizontal += amount
            vertical += aim * amount
        else:
            if direction == "up":
                amount = -1 * amount
            aim += amount
    return vertical, horizontal


def get_aimed_distance_product(directions: list[tuple[str, int]]) -> int:
    vertical, horizontal = get_aimed_positions(directions)
    return vertical * horizontal


if __name__ == "__main__":
    directions = parse_file("data/day2.txt")
    print(get_aimed_distance_product(directions))
