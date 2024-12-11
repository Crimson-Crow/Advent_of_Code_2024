# Advent of Code 2024 Day 11
import time
import pathlib
import math
from collections import defaultdict

cache = {}
def split(stone: int, num_digits: int) -> tuple[int, int]:
    if stone in cache:
        return cache[stone]
    divisor = 10 ** (num_digits // 2)
    result = stone // divisor, stone % divisor
    cache[stone] = result
    return result

def blink(stones: dict[int, int]) -> dict[int, int]:
    stones_new = defaultdict(int)
    for stone, count in stones.items():
        if stone:
            num_digits = math.floor(math.log10(stone)) + 1
            if num_digits % 2:
                stones_new[2024 * stone] += count
            else:
                a, b = split(stone, num_digits)
                stones_new[a] += count
                stones_new[b] += count
        else:
            stones_new[1] += count
    return stones_new

iterations = 75
stones_list = map(int, pathlib.Path("input.txt").read_text().split())
stones = defaultdict(int)
for stone in stones_list:
    stones[stone] += 1

for _ in range(iterations):
    stones = blink(stones)
print(sum(stones.values()))