from advent_of_code.day2.part1 import get_distance_product
from advent_of_code.day2.part2 import get_aimed_distance_product


def test_part1() -> None:

    directions = [
        ("forward", 5),
        ("down", 5),
        ("forward", 8),
        ("up", 3),
        ("down", 8),
        ("forward", 2),
    ]

    distance_product = get_distance_product(directions)

    assert distance_product == 150


def test_part2() -> None:

    directions = [
        ("forward", 5),
        ("down", 5),
        ("forward", 8),
        ("up", 3),
        ("down", 8),
        ("forward", 2),
    ]

    distance_product = get_aimed_distance_product(directions)

    assert distance_product == 900
