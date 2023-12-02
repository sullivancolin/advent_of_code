"""
The total disk space available to the filesystem is 70000000. To run the update, you need unused space of at least 30000000. You need to find a directory you can delete that will free up enough space to run the update.

In the example above, the total size of the outermost directory (and thus the total amount of used space) is 48381165; this means that the size of the unused space must currently be 21618835, which isn't quite the 30000000 required by the update. Therefore, the update still requires a directory with total size of at least 8381165 to be deleted before it can run.

To achieve this, you have the following options:

    Delete directory e, which would increase unused space by 584.
    Delete directory a, which would increase unused space by 94853.
    Delete directory d, which would increase unused space by 24933642.
    Delete directory /, which would increase unused space by 48381165.

Directories e and a are both too small; deleting them would not free up enough space. However, directories d and / are both big enough! Between these, choose the smallest: d, increasing unused space by 24933642.

Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. What is the total size of that directory?
"""

from advent_of_code.day7.part1 import populate_file_tree


def smallest_dir_to_free_size(input_str: str) -> int:
    directory_dict = populate_file_tree(input_str)
    total_used = directory_dict["/"].total_size
    free = 70_000_000 - total_used
    to_free = 30_000_000 - free

    ds = sorted(list(directory_dict.values()), key=lambda d: d.total_size)
    for d in ds:
        if d.total_size > to_free:
            return d.total_size
    return 0


if __name__ == "__main__":
    input_str = open("data/day7.txt").read()

    total_directory_size = smallest_dir_to_free_size(input_str)
    print(total_directory_size)
