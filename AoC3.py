# Advent of Code 2024 Day 3
import pathlib
import re

input_data = pathlib.Path("input.txt").read_text()

# Part 1
PATTERN = r"mul\((\d{1,3}),(\d{1,3})\)"
compute = lambda s: sum(int(x)*int(y) for x, y in re.findall(PATTERN, s))
print(compute(input_data))

# Part 2
INSTRUCTION_PATTERN = r"don't\(\).*?(?:do\(\)|$)"

print(compute(re.sub(INSTRUCTION_PATTERN, '', input_data, flags=re.DOTALL)))