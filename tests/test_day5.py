from advent_of_code.day5.part1 import Point, get_number_overlaps, get_shape

line_endpoints = [
    (Point(0, 9), Point(5, 9)),
    (Point(8, 0), Point(0, 8)),
    (Point(9, 4), Point(3, 4)),
    (Point(2, 2), Point(2, 1)),
    (Point(7, 0), Point(7, 4)),
    (Point(6, 4), Point(2, 0)),
    (Point(0, 9), Point(2, 9)),
    (Point(3, 4), Point(1, 4)),
    (Point(0, 0), Point(8, 8)),
    (Point(5, 5), Point(8, 2)),
]


def test_get_number_overlaps() -> None:
    assert get_number_overlaps(line_endpoints) == 5


def test_get_shape() -> None:
    assert get_shape(line_endpoints) == (10, 10)
