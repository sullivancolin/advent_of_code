"""
It seems like the X register controls the horizontal position of a sprite. Specifically, the sprite is 3 pixels wide, and the X register sets the horizontal position of the middle of that sprite. (In this system, there is no such thing as "vertical position": if the sprite's horizontal position puts its pixels where the CRT is currently drawing, then those pixels will be drawn.)

You count the pixels on the CRT: 40 wide and 6 high. This CRT screen draws the top row of pixels left-to-right, then the row below that, and so on. The left-most pixel in each row is in position 0, and the right-most pixel in each row is in position 39.

Like the CPU, the CRT is tied closely to the clock circuit: the CRT draws a single pixel during each cycle. Representing each pixel of the screen as a #, here are the cycles during which the first and last pixel in each row are drawn:

Cycle   1 -> ######################################## <- Cycle  40
Cycle  41 -> ######################################## <- Cycle  80
Cycle  81 -> ######################################## <- Cycle 120
Cycle 121 -> ######################################## <- Cycle 160
Cycle 161 -> ######################################## <- Cycle 200
Cycle 201 -> ######################################## <- Cycle 240

So, by carefully timing the CPU instructions and the CRT drawing operations, you should be able to determine whether the sprite is visible the instant each pixel is drawn. If the sprite is positioned such that one of its three pixels is the pixel currently being drawn, the screen produces a lit pixel (#); otherwise, the screen leaves the pixel dark (.).

Allowing the program to run to completion causes the CRT to produce the following image:

##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....


Render the image given by your program. What eight capital letters appear on your CRT?
"""
import numpy as np


def get_pixel_val(sprite_location: np.ndarray, curr_cycle: int) -> str:
    old_cycle = curr_cycle
    if old_cycle == 175:
        old_cycle
    if curr_cycle > 40:
        curr_cycle = curr_cycle % 40
    if any(sprite_location == curr_cycle - 1):
        pixel = "#"
    else:
        pixel = "."
    if curr_cycle % 40 == 0:
        pixel += "\n"
    return pixel


def print_screen(input_str: str) -> str:
    instructions = [
        0 if line == "noop" else int(line.split()[1]) for line in input_str.split("\n")
    ]

    sprite_location = np.array([0, 1, 2])
    curr_cycle = 0
    pixels = []

    for instruction in instructions:
        curr_cycle += 1
        pixel_val = get_pixel_val(sprite_location, curr_cycle)
        pixels.append(pixel_val)
        if instruction:
            curr_cycle += 1
            pixel_val = get_pixel_val(sprite_location, curr_cycle)
            pixels.append(pixel_val)
            sprite_location += instruction
    return "".join(pixels)


if __name__ == "__main__":
    input_str = open("data/day10.txt").read()

    print(print_screen(input_str))
