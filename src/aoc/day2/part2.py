"""
The Elf says they've stopped producing snow because they aren't getting any water! He isn't sure why the water stopped; however, he can show you how to get to the water source to check it out for yourself. It's just up ahead!

As you continue your walk, the Elf poses a second question: in each game you played, what is the fewest number of cubes of each color that could have been in the bag to make the game possible?

Again consider the example games from earlier:

```
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
```

- In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes. If any color had even one fewer cube, the game would - have been impossible.
- Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
- Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
- Game 4 required at least 14 red, 3 green, and 15 blue cubes.
- Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.

The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up these five powers produces the sum 2286.

For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?

# Solution:
"""


from aoc.day2.part1 import Draw, draw_pattern


def game_power(draws: list[Draw]) -> int:
    """Calculate the largest value for each color from all the draws.

    Args:
        draws: list of Draws in the game

    Returns:
        Maximum color values multiplied together
    """
    max_r = 0
    max_g = 0
    max_b = 0
    for draw in draws:
        if draw.red > max_r:
            max_r = draw.red
        if draw.green > max_g:
            max_g = draw.green
        if draw.blue > max_b:
            max_b = draw.blue
    return max_r * max_g * max_b


def sum_game_powers(input_text: str) -> int:
    """Parse each line into Game with draws. Find the minumum required cubes of each color and multiply together to get the game power and calculate the cumulative sum.

    Args:
        input_text: Raw input text.

    Returns:
        sum of all game powrs
    """

    lines = input_text.splitlines()
    cum_sum = 0
    for line in lines:
        draw_strings = line.split(": ")[1].split("; ")
        draws = []
        for ds in draw_strings:
            draws.append(
                Draw(**{color: int(count) for count, color in draw_pattern.findall(ds)})
            )

        cum_sum += game_power(draws)
    return cum_sum
