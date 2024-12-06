# Advent of Code 2024 Day 6
import pathlib
from collections import defaultdict

grid = [list(s) for s in pathlib.Path("input.txt").read_text().splitlines()]
directions = ((-1, 0), (0, 1), (1, 0), (0, -1))  # Up, Right, Down, Left

# Part 1
def get_guard_info(grid):
    guard_char = ("^", ">", "V", "<")
    for list_index, s in enumerate(grid):
        for i, char in enumerate(guard_char):
            try:
                return (list_index, s.index(char)), i
            except ValueError:
                continue                

def traverse(grid, pos, direction):
    visited = defaultdict(set)
    infinite = True
    try:
        while True:
            visited_pos = visited[pos]
            if direction in visited_pos:  # Infinite
                break
            visited_pos.add(direction)
            for _ in range(4):
                new_pos = tuple(a + b for a, b in zip(directions[direction], pos))
                if new_pos[0] < 0 or new_pos[1] < 0:
                    raise IndexError
                if grid[new_pos[0]][new_pos[1]] != "#":
                    pos = new_pos
                    break
                direction = (direction + 1) % 4
            else:  # Edge case: obstacles in 4 directions
                break
    except IndexError:
       infinite = False
    return visited.keys(), infinite

guard_pos, guard_direction = get_guard_info(grid)
visited = traverse(grid, guard_pos, guard_direction)[0]
print(len(visited))

# Part 2
import sys
import copy

possible_obstacle_positions = set(visited)
possible_obstacle_positions.remove(guard_pos)
total_positions = float(len(possible_obstacle_positions))
count = 0
for i, pop in enumerate(possible_obstacle_positions):
    sys.stdout.write(f"\r{100 * (i / total_positions):.1f}% Complete")
    sys.stdout.flush()
    new_grid = copy.deepcopy(grid)
    new_grid[pop[0]][pop[1]] = "#"
    count += traverse(new_grid, guard_pos, guard_direction)[1]
print()
print(count)