# Wrong approach lol I filled my RAM

import math
from numba import njit, types
from numba.typed import List, Dict

SplitTuple = types.UniTuple(types.uint64, 2)
Cache = types.DictType(types.uint64, SplitTuple)
StoneList = types.ListType(types.uint64)

@njit(SplitTuple(Cache, types.uint64, types.uint8), fastmath=True)
def split(cache, stone, num_digits):
    if stone in cache:
        return cache[stone]
    divisor = 10 ** (num_digits // 2)
    result = stone // divisor, stone % divisor
    cache[stone] = result
    return result

@njit(StoneList(StoneList, Cache), fastmath=True)
def blink(stones, cache):
    results = List.empty_list(types.uint64)
    for stone in stones:
        if stone:
            num_digits = math.floor(math.log10(stone)) + 1
            if num_digits % 2:
                results.append(2024 * stone)
            else:
                results.extend(split(cache, stone, num_digits))
        else:
            results.append(1)
    return results

@njit(cache=True, fastmath=True)
def blink_loop(stones_in, iterations):
    cache = Dict.empty(
        key_type=types.uint64,
        value_type=SplitTuple,
    )
    stones = List.empty_list(types.uint64)
    for stone in stones_in:
        stones.append(stone)

    for _ in range(iterations):
        stones = blink(stones, cache)
    return stones

# Stones = types.DictType(types.uint64, types.uint64)

# @njit(types.void(Stones, types.uint64, types.uint64), fastmath=True)
# def increment(stones, value, count):
    # if value not in stones:
        # stones[value] = count
    # else:
        # stones[value] += count

# @njit(types.UniTuple(types.uint64, 2)(types.uint64, types.uint8), fastmath=True)
# def split(stone, num_digits):
    # # if stone in cache:
        # # return cache[stone]
    # divisor = 10 ** (num_digits // 2)
    # result = stone // divisor, stone % divisor
    # # cache[stone] = result
    # return result

# @njit(Stones(Stones), fastmath=True)
# def blink(stones):
    # stones_new = Dict.empty(
        # key_type=types.uint64,
        # value_type=types.uint64,
    # )
    # for stone, count in stones.items():
        # if stone:
            # num_digits = math.floor(math.log10(stone)) + 1
            # if num_digits % 2:
                # increment(stones_new, 2024 * stone, count)
            # else:
                # left, right = split(stone, num_digits)
                # increment(stones_new, left, count)
                # increment(stones_new, right, count)
        # else:
            # increment(stones_new, 1, count)
    # return stones_new

# @njit(cache=True, fastmath=True)
# def blink_optimized_loop(stone_list, iterations):
    # stones = Dict.empty(
        # key_type=types.uint64,
        # value_type=types.uint64,
    # )
    # for stone in stone_list:
        # increment(stones, stone, 1)

    # for _ in range(iterations):
        # stones = blink(stones)
    # return stones