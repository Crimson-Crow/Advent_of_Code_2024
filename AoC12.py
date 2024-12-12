# Advent of Code 2024 Day 12
import pathlib

grid = list(map(list, pathlib.Path("input.txt").read_text().splitlines()))
rows, cols = len(grid), len(grid[0])
visited = [[False] * cols for _ in range(rows)]
DIRECTIONS = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

def is_part_of_zone(x, y, char):
    return 0 <= x < rows and 0 <= y < cols and grid[x][y] == char

def dfs(x, y, char):
    stack = [(x, y)]
    visited[x][y] = True
    area = 0
    perimeter = 0
    edges = 0
    
    while stack:
        cx, cy = stack.pop()
        area += 1
        tile_in_zone = [is_part_of_zone(cx + dir[0], cy + dir[1], char) for dir in DIRECTIONS]
        for i in range(0, 8, 2):  # Iterate non-diagonal tiles            
            if tile_in_zone[i]:
                dir = DIRECTIONS[i]
                nx, ny = cx + dir[0], cy + dir[1]
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    stack.append((nx, ny))
                # CONCAVE CORNER
                if not tile_in_zone[i-1] and tile_in_zone[i-2]:
                    edges += 1
            else:
                perimeter += 1
                # CONVEX CORNER
                if not tile_in_zone[i-2]:
                    edges += 1
    return area, perimeter, edges

part_1 = 0
part_2 = 0
for i in range(rows):
    for j in range(cols):
        if not visited[i][j]:  # Flood-fill new zone
            char = grid[i][j]
            area, perimeter, sides = dfs(i, j, char)
            part_1 += area * perimeter
            part_2 += area * sides
print(part_1)
print(part_2)