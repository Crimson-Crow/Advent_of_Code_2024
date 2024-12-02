# Advent of Code 2024 Day 2
import pathlib

input_data = pathlib.Path("input.txt").read_text()

reports = [list(map(int, s.split())) for s in input_data.splitlines()]

# Part 1
def is_valid_report(report):
    return (
        (report == sorted(report) or report == sorted(report, reverse=True))  # Condition 1
        and all(1 <= abs(b - a) <= 3 for a, b in zip(report, report[1:]))     # Condition 2
    )

safe_count = 0
for report in reports:
    if is_valid_report(report):
        safe_count += 1
print(safe_count)

# Part 2
safe_count = 0
for report in reports:
    if is_valid_report(report):
        safe_count += 1
    else:  # Brute force, not optimal :(
        for missing_item_report in [report[:i] + report[i+1:] for i in range(len(report))]:
            if is_valid_report(missing_item_report):
                safe_count += 1
                break
print(safe_count)