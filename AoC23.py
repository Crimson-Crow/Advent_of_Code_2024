# Advent of Code 2024 Day 23
from collections import defaultdict

input = [line.split("-") for line in open("input.txt").read().splitlines()]

def find_triangles(pairs):
    graph = defaultdict(set)
    for a, b in pairs:
        graph[a].add(b)
        graph[b].add(a)
    
    triangles = set()
    for a in graph:
        for b in graph[a]:
            common_neighbors = graph[a].intersection(graph[b])
            for c in common_neighbors:
                triangle = tuple(sorted([a, b, c]))
                triangles.add(triangle)
    
    return triangles

print(sum(any(computer.startswith("t") for computer in triangle) for triangle in find_triangles(input)))