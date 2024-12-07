# Advent of Code 2024 Day 7
import pathlib
import itertools

input_data = pathlib.Path("input.txt").read_text().replace(":", "")

# Part 1
total = 0
for line in input_data.splitlines():
    test_value, *values = map(int, line.split())
    for ops in itertools.product("*+", repeat=len(values)-1):
        acc = values[0]
        for val, op in zip(values[1:], ops):
            if op == "*":
                acc *= val
            else:
                acc += val
        if acc == test_value:
            total += test_value
            break
print(total)

# Part 2
total = 0
for line in input_data.splitlines():
    test_value, *values = map(int, line.split())
    for ops in itertools.product("*+|", repeat=len(values)-1):
        acc = values[0]
        for val, op in zip(values[1:], ops):
            if op == "*":
                acc *= val
            elif op == "+":
                acc += val
            else:
                acc = int(str(acc) + str(val))
        if acc == test_value:
            total += test_value
            break
print(total)