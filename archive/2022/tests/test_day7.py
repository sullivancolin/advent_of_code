from advent_of_code.day7.part1 import get_total_directory_sizes
from advent_of_code.day7.part2 import smallest_dir_to_free_size

input_str = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""


def test_get_total_directory_sizes() -> None:
    result = get_total_directory_sizes(input_str)
    assert result == 95437


def test_smallest_dir_to_free() -> None:
    result = smallest_dir_to_free_size(input_str)
    assert result == 24933642
