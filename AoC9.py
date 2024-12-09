# Advent of Code 2024 Day 9
import pathlib

disk_map = pathlib.Path("input.txt").read_text()

id = -1
disk = [(None if i % 2 else (id := id + 1), count) for i, char in enumerate(disk_map) if (count := int(char)) != 0]

# Part 1
copy = [id for id, count in disk for _ in range(count)]
try:
    while True:
        empty_index = copy.index(None)
        if v := copy.pop():
            copy[empty_index] = v
except ValueError:
    print(sum(i * v for i, v in enumerate(copy)))