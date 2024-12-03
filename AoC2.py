# Advent of Code 2024 Day 2
import pathlib

input_data = pathlib.Path("input.txt").read_text()

reports = [list(map(int, s.split())) for s in input_data.splitlines()]

# Part 1
def is_valid_report(report):
    it = tuple(zip(report, report[1:]))
    return all(1 <= b - a <= 3 for a, b in it) or all(1 <= a - b <= 3 for a, b in it)

print(sum(is_valid_report(report) for report in reports))

# Part 2
print(
    sum(
        is_valid_report(report)
        or any(  # Brute force, not optimal :(
            is_valid_report(report[:i] + report[i+1:]) for i in range(len(report))
        )
        for report in reports
    )
)
