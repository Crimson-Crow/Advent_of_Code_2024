# Advent of Code 2024 Day 15
from operator import add

warehouse, moves = open("input.txt").read().split("\n\n")
warehouse = warehouse.splitlines()
moves = moves.replace("\n", "")

walls = set()
initial_boxes = []

for row_idx, row in enumerate(warehouse):
    for col_idx, char in enumerate(row):
        if char == "#":
            walls.add((row_idx, col_idx))
        elif char == "O":
            initial_boxes.append((row_idx, col_idx))
        elif char == "@":
            robot = (row_idx, col_idx)

ew_add = lambda l1, l2: tuple(map(add, l1, l2))

# Part 1
boxes = initial_boxes.copy()
MOVES_TRANSLATE = {"<": (0, -1), "^": (-1, 0), ">": (0, 1), "v": (1, 0)}
for delta_pos in (MOVES_TRANSLATE[c] for c in moves):
    pos = robot
    apply_move_candidates = []
    while True:
        pos = ew_add(pos, delta_pos)
        if pos in walls:
            break
        elif pos in boxes:
            apply_move_candidates.append(boxes.index(pos))
        else:
            robot = ew_add(robot, delta_pos)
            for box_idx in apply_move_candidates:
                boxes[box_idx] = ew_add(boxes[box_idx], delta_pos)
            break
print(sum(100 * r + c for r, c in boxes))

# Part 2