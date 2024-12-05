# Advent of Code 2024 Day 5
import pathlib

input_data = pathlib.Path("input.txt").read_text().splitlines()
section_delim = input_data.index("")
rules = {}
for a, b in (map(int, s.split("|")) for s in input_data[:section_delim]):
    if a not in rules:
        rules[a] = []
    rules[a].append(b)
updates = [tuple(map(int, s.split(","))) for s in input_data[section_delim+1:]]

# Part 1
invalid_updates = []
valid_updates = []
for update in updates:
    if any(page in rules and any(rule in update[:i] for rule in rules[page]) for i, page in enumerate(update)):
        invalid_updates.append(update)
    else:
        valid_updates.append(update)

print(sum(update[len(update) // 2] for update in valid_updates))

# Part 2
count = 0
for update in invalid_updates:
    placed = set()
    sorted_update = []

    while len(placed) < len(update):
        for num in update:
            if num in placed:
                continue
            
            if all(before not in update or before in placed for before in rules if num in rules[before]):
                sorted_update.append(num)
                placed.add(num)
                break
    count += sorted_update[len(update) // 2]
print(count)