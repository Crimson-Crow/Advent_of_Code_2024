# Advent of Code 2024 Day 10
import pathlib
from collections import deque, defaultdict

height_map = [list(map(int, line)) for line in pathlib.Path("input.txt").read_text().splitlines()]
rows, cols = len(height_map), len(height_map[0])
starts = [(x, y) for x in range(rows) for y in range(cols) if height_map[x][y] == 0]
DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))

def is_valid(x, y, current_height):
    return (
        0 <= x < rows and 
        0 <= y < cols and 
        height_map[x][y] == current_height + 1
    )

# Part 1
def bfs(start):
    visited = set()
    queue = deque([start])
    reachable = set()
    
    while queue:
        x, y = queue.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        
        current_height = height_map[x][y]
        
        if current_height == 9:
            reachable.add((x, y))
            continue
        
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, current_height) and (nx, ny) not in visited:
                queue.append((nx, ny))
    
    return len(reachable)

print(sum(bfs(start) for start in starts))

# Part 2
def bfs(start):
    queue = deque([(start[0], start[1], 0)])
    path_counts = defaultdict(int)
    
    while queue:
        x, y, current_height = queue.popleft()
        
        if current_height == 9:
            path_counts[(x, y)] += 1
            continue
        
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, current_height):
                queue.append((nx, ny, height_map[nx][ny]))
    
    return sum(path_counts.values())

print(sum(bfs(start) for start in starts))