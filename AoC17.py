# Advent of Code 2024 Day 17
from itertools import count
import numpy as np
from numba import njit, types, prange
from numba.typed import List

input = open("input.txt").read().splitlines()

registers = np.array([int(line[12:]) for line in input[:3]], dtype=np.uint64)
instructions = np.array(tuple(map(int, input[-1][8:].split(","))), dtype=np.uint8)
prog_len = len(instructions)

@njit("u8(u1, u8[:])")
def to_lit_operand(i, registers):
    if 0 <= i <= 3:
        return i
    elif i == 4:
        return registers[0]
    elif i == 5:
        return registers[1]
    elif i == 6:
        return registers[2]
    raise ValueError

@njit("u1[:](u8[:], u1[:])")
def run_program(registers, instructions):
    output = List.empty_list(types.uint8)
    ip = 0
    while ip < prog_len:
        opcode = instructions[ip]
        operand = instructions[ip + 1]
        if opcode == 0: # adv
            registers[0] >>= to_lit_operand(operand, registers)
        elif opcode == 1: # bxl
            registers[1] ^= operand
        elif opcode == 2: # bst
            registers[1] = to_lit_operand(operand, registers) & 0b111
        elif opcode == 3 and registers[0] != 0: # jnz
            ip = operand
            continue
        elif opcode == 4: # bxc
            registers[1] ^= registers[2]
        elif opcode == 5: # out
            output.append(to_lit_operand(operand, registers) & 0b111)
        elif opcode == 6: # bdv
            registers[1] = registers[0] >> to_lit_operand(operand, registers)
        elif opcode == 7: # cdv
            registers[2] = registers[0] >> to_lit_operand(operand, registers)
        ip += 2
    a = np.empty(len(output), dtype=output._dtype)
    for i, v in enumerate(output):
        a[i] = v
    return a

# Part 1
print(run_program(registers, instructions))

# Part 2: Bruteforce doesn't work :(
from time import perf_counter

t0 = perf_counter()

@njit("u8(u1[:])")
def part_b(instructions):
    i = 1_000_000_000_000
    while True:
        registers = np.zeros(3, dtype=np.uint64)
        registers[0] = i
        output = run_program(registers, instructions)
        if np.array_equal(instructions, output):
            break
        i += 1
    return i
print(part_b(instructions))
print(perf_counter() - t0)