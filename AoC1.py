# Advent of Code 2024 Day 1
import pathlib

input_data = pathlib.Path("input.txt").read_text()

l1, l2 = zip(*(map(int, line.split()) for line in input_data.splitlines()))

# Part 1
print(sum(abs(x - y) for x, y in zip(sorted(l1), sorted(l2))))

# Part 2
from collections import Counter
count = Counter(l2)
print(sum(x*count[x] for x in l1))