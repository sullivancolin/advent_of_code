from advent_of_code.day6.part1 import signal_start_position

input_str = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"


def test_signal_start_position() -> None:
    result = signal_start_position(input_str)
    assert result == 7


def test_message_start_position() -> None:
    result = signal_start_position(input_str, window_size=14)
    assert result == 19
