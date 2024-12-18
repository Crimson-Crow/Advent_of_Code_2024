# Advent of Code 2024 Day 16
import heapq
from collections import defaultdict

maze = open("input.txt").read().splitlines()
walls = set()
#0 = Up, 1 = Right, 2 = Down, 3 = Left
DIRECTIONS = ((-1, 0), (0, 1), (1, 0), (0, -1))

for row_idx, row in enumerate(maze):
    for col_idx, char in enumerate(row):
        if char == "#":
            walls.add((row_idx, col_idx))
        elif char == "S":
            start = (row_idx, col_idx)
        elif char == "E":
            end = (row_idx, col_idx)

add = lambda l1, l2: (l1[0] + l2[0], l1[1] + l2[1])

def find_optimal_paths(walls, start, end):
    start_state = (start, 1)
    pq = [(0, *start_state)]
    
    min_cost = defaultdict(lambda: float('inf'))
    min_cost[start_state] = 0
    parent = defaultdict(list)
    goal_cost = float('inf')
    
    while pq:
        cost, pos, direction = heapq.heappop(pq)
        
        if cost > goal_cost:
            continue

        if pos == end:
            goal_cost = min(goal_cost, cost)
            continue
        
        # Move forward
        if (new_pos := add(pos, DIRECTIONS[direction])) not in walls:
            new_cost = cost + 1
            new_state = (new_pos, direction)
            if new_cost < min_cost[new_state]:
                min_cost[new_state] = new_cost
                heapq.heappush(pq, (new_cost, *new_state))
                parent[new_state] = [(pos, direction)]
            elif new_cost == min_cost[new_state]:
                parent[new_state].append((pos, direction))
        
        # Rotate
        new_cost = cost + 1000
        for turn in (-1, 1):
            new_state = (pos, (direction + turn) % 4)
            if new_cost < min_cost[new_state]:
                min_cost[new_state] = new_cost
                heapq.heappush(pq, (new_cost, *new_state))
                parent[new_state] = [(pos, direction)]
            elif new_cost == min_cost[new_state]:
                parent[new_state].append((pos, direction))
    
    optimal_paths = []
    
    def backtrack(pos, direction, path):
        if (pos, direction) == start_state:
            optimal_paths.append(set(path))
            return
        for prev_pos, pdir in parent[(pos, direction)]:
            backtrack(prev_pos, pdir, path + [pos])
    
    for d in range(4):
        if min_cost[(end, d)] == goal_cost:
            backtrack(end, d, [end])
    
    return goal_cost, optimal_paths

cost, paths = find_optimal_paths(walls, start, end)
print(cost)
print(len(set.union(*paths)))