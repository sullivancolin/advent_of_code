"""
To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.

In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these three elves is 45000.

Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
"""
from heapq import nlargest


def calculate_top_3_total_calories(inventory_text: str) -> int:
    return sum(
        nlargest(
            3,
            (
                sum(map(int, sublist.split("\n")))
                for sublist in inventory_text.split("\n\n")
            ),
        )
    )


if __name__ == "__main__":
    with open("data/day1.txt") as infile:
        inventory_text = infile.read()

    total_calories = calculate_top_3_total_calories(inventory_text)
    print(total_calories)
