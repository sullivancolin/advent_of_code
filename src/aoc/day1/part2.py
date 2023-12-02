"""
# Part Two

Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

```sh
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
```

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?

## Solution:
"""
import re

word_to_digit = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

word_pattern = re.compile(
    r"(?=(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)|(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|(9))"
)


def word_calibration_sum(text: str) -> int:
    """
    * Split input on newline
    * iterate over lines
    * extract word digts
    * convert to integer strings
    * concatenate
    * converte to integers
    *  then sum.

    Args:
        text: Raw input text.

    Returns:
        sum of all the concatenated first and last word numbers of each line.

    """
    lines = text.strip().split("\n")
    nums = []
    for line in lines:
        matches: list[tuple[str, ...]] = word_pattern.findall(line)
        digit_words = [word for tup in matches for word in tup if word]
        digit_1 = digit_words[0]
        digit_2 = digit_words[-1]
        if digit_1 in word_to_digit:
            digit_1 = word_to_digit[digit_1]
        if digit_2 in word_to_digit:
            digit_2 = word_to_digit[digit_2]
        nums.append(int("".join([digit_1, digit_2])))
    return sum(nums)
