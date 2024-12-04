# Advent of Code 2024 Day 4
import pathlib

input_data = pathlib.Path("input.txt").read_text()

# Part 1
grid = input_data.splitlines()
rows, cols = len(grid), len(grid[0])
word = "XMAS"
word_len = len(word)

DIRECTIONS = (
    (-1, 0), (1, 0),  # vertical
    (0, -1), (0, 1),  # horizontal
    (-1, -1), (1, 1), (-1, 1), (1, -1)  # diagonal
)

count = 0
for start_r in range(rows):
    for start_c in range(cols):
        if grid[start_r][start_c] == "X":
            for dr, dc in DIRECTIONS:
                # Bounds check
                if (dr < 0 and start_r < word_len - 1) or \
                   (dr > 0 and start_r > rows - word_len) or \
                   (dc < 0 and start_c < word_len - 1) or \
                   (dc > 0 and start_c > cols - word_len):
                    continue
                
                r = start_r + dr
                c = start_c + dc
                for l in word[1:]:
                    if grid[r][c] != l:
                        break
                    r += dr
                    c += dc
                else:
                    count += 1
print(count)

# PART 2
PATTERN = (("M", "S"), ("S", "M"))

print(
    sum(
        grid[row][col] == "A"
        and (grid[row - 1][col - 1], grid[row + 1][col + 1]) in PATTERN
        and (grid[row - 1][col + 1], grid[row + 1][col - 1]) in PATTERN
        for row in range(1, rows - 1)
        for col in range(1, cols - 1)
    )
)