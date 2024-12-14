# Advent of Code 2024 Day 14
import re
import itertools
import math

robots = tuple(itertools.batched(map(int, re.findall(r"-?\d+", open("input.txt").read())), 4))
WIDTH, HEIGHT = 101, 103
MIDDLE_X, MIDDLE_Y = WIDTH // 2, HEIGHT // 2

def sim(t, px, py, vx, vy):
    return (px + t * vx) % WIDTH, (py + t * vy) % HEIGHT

# Part 1
quadrants = [0, 0, 0, 0]
for robot in robots:
    x, y = sim(100, *robot)
    if (x := x - MIDDLE_X) and (y := y - MIDDLE_Y):
        quadrants[(x > 0) | (y > 0) << 1] += 1
print(math.prod(quadrants))

# Part 2
def find_tree(robots):
    for i in range(WIDTH * HEIGHT):
        robot_positions = {sim(i, *robot) for robot in robots}
        for y in range(HEIGHT):
            contiguous = 0
            for x in range(WIDTH):
                contiguous = contiguous + 1 if (x, y) in robot_positions else 0
                if contiguous == 30:
                    return i
    return -1

def print_grid(i):
    grid = [list("." * WIDTH) for row in range(HEIGHT)]
    for x, y in [sim(i, *robot) for robot in robots]:
        grid[y][x] = "X"
    for row in grid:
        print("".join(row))

t = find_tree(robots)
print_grid(t)
print(t)
