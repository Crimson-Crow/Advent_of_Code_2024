# Advent of Code 2024 Day 18
from collections import deque

input = open("input.txt").read().splitlines()
bytes_list = [tuple(map(int, line.split(","))) for line in input]
rows, cols = 71, 71
directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

# Part 1
obstacles = set(bytes_list[:1024])
def min_steps(start, end):
    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        pos, steps = queue.popleft()
        if pos == end:
            return steps
        for dx, dy in directions:
            new_pos = pos[0] + dx, pos[1] + dy
            if 0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols and new_pos not in obstacles and new_pos not in visited:
                queue.append((new_pos, steps + 1))
                visited.add(new_pos)
    return -1

print(min_steps((0, 0), (rows-1, cols-1)))

# Part 2
top_right = []
bottom_left = []
unconnected = []

def is_neighbor(pos, group):
    x, y = pos
    for g_x, g_y in group:
        if -1 <= g_x - x <= 1 and -1 <= g_y - y <= 1:
            return True
    return False

for pos in bytes_list:
    is_top_right = pos[0] == cols - 1 or pos[1] == 0 or is_neighbor(pos, top_right)
    is_bottom_left = pos[0] == 0 or pos[1] == rows - 1 or is_neighbor(pos, bottom_left)
    
    if is_top_right and is_bottom_left:
        print(pos)
        break

    if is_top_right:
        top_right.append(pos)
    elif is_bottom_left:
        bottom_left.append(pos)
    
    groups = {True: [], False: []}
    for sublist in unconnected:
        groups[is_neighbor(pos, sublist)].append(sublist)
    nb_true = len(groups[True])
    if nb_true >= 1:
        merged = sum(groups[True], [])
        if is_top_right:
            top_right.extend(merged)
            unconnected = groups[False]
        elif is_bottom_left:
            bottom_left.extend(merged)
            unconnected = groups[False]
        else:
            merged.append(pos)
            unconnected = [merged] + groups[False]
    elif not (is_top_right or is_bottom_left):
        unconnected.append([pos])
