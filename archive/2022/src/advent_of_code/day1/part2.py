"""
To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.

In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these three elves is 45000.

Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
"""
from functools import partial
from heapq import nlargest

top_3 = partial(nlargest, 3)


def calculate_top_3_total_calories(all_elf_inventories: str) -> int:
    return sum(
        top_3(
            sum(
                int(calorie_string)
                for calorie_string in elf_inventory_string.split("\n")
            )
            for elf_inventory_string in all_elf_inventories.split("\n\n")
        )
    )


if __name__ == "__main__":
    with open("data/day1.txt") as infile:
        inventory_text = infile.read()

    total_calories = calculate_top_3_total_calories(inventory_text)
    print(total_calories)
