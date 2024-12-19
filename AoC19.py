# Advent of Code 2024 Day 19
input = open("input.txt").read().splitlines()
patterns = tuple(input[0].split(", "))

def count_combinations(s: str) -> int:
    cache = {}
    s_len = len(s)
    def matches(subseq: str, index: int) -> bool:
        end_index = index + len(subseq)
        return end_index <= s_len and subseq == s[index:end_index]

    def dp(index: int) -> int:
        if index == s_len:
            return 1
        if index in cache:
            return cache[index]
        count = sum(dp(index + len(p)) for p in patterns if matches(p, index))
        cache[index] = count
        return count

    return dp(0)

combinations = [count_combinations(s) for s in input[2:]]
print(sum(map(bool, combinations)))
print(sum(combinations))
