# Advent of Code 2024 Day 8
import pathlib
import itertools
from collections import defaultdict

grid = pathlib.Path("input.txt").read_text().splitlines()

rows, cols = len(grid), len(grid[0])
network = defaultdict(list)
for r, line in enumerate(grid):
    for c, char in enumerate(line):
        if char != ".":
            network[char].append((r, c))

# Part 1
antinodes = set()
for antennas in network.values():
    if len(antennas) == 1:
        continue
    for a, b in itertools.permutations(antennas, 2):
        r = 2 * a[0] - b[0]
        c = 2 * a[1] - b[1]
        if 0 <= r < rows and 0 <= c < cols:
            antinodes.add((r, c))
print(len(antinodes))

# Part 2
antinodes = set()
for antennas in network.values():
    if len(antennas) == 1:
        continue
    for a, b in itertools.combinations(antennas, 2):
        antinodes.add(a)
        dr = b[0] - a[0]
        dc = b[1] - a[1]
        for dr, dc in ((dr, dc), (-dr, -dc)):  # Scan towards and away from antenna b
            r = a[0]
            c = a[1]
            while True:
                r += dr
                c += dc
                if not (0 <= r < rows and 0 <= c < cols):
                    break
                antinodes.add((r, c))
print(len(antinodes))
