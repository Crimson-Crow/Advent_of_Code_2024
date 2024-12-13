# Advent of Code 2024 Day 13
import pathlib
import re
import itertools
from scipy.optimize import linprog
import numpy as np

c = np.array([3, 1])
def solve(ax, ay, bx, by, px, py, max=None):
    A_eq = np.array([[ax, bx], [ay, by]])  # Coefficients for x and y
    b_eq = np.array([px, py])

    bounds = [(0, max), (0, max)] if max else [(0, None), (0, None)]

    result = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds)

    if result.success:
        a, b = map(int, map(round, result.x))
        if (ax * a + bx * b == px) and (ay * a + by * b == py):
            return 3 * a + b
    return 0

arcade = list(itertools.batched(map(int, re.findall(r'[+=](\d+)', pathlib.Path("input.txt").read_text())), 6))
print(sum(solve(*params, max=100) for params in arcade))
error = 10000000000000
print(sum(solve(ax, ay, bx, by, px + error, py + error) for ax, ay, bx, by, px, py in arcade))