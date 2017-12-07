#!/usr/bin/env python3

import utils

def cycle(memory):
    """Finds the largest value in memory and redistributes to other addresses.

    When finding the largest value, ties are resolved by taking the lowest 
    index. That index is set to 0, and then the next n addresses are incremented
    by one, where n is the largest value that was found (looping back to the 
    start of the array if required).

    Args:
        memory: A list of ints representing memory addresses and their contents.
    """
    max_value = max(memory)
    index = memory.index(max_value)
    memory[index] = 0
    for _ in range(max_value):
        if index == (len(memory) - 1):
            index = 0
        else:
            index += 1
        memory[index] += 1

def reallocate(memory):
    """Calculates the number of cycles and cycle length until state is repeated.

    Performs memory reallocation cycles until a repeated state is reached, and 
    finds how many cycles this takes, as well as the length of the cycle.

    Args:
        memory: A list of ints representing memory addresses and their contents.

    Returns:
        A tuple of how many cycles were performed and the cycle length.
    """
    memory = memory[:]
    states = {} 
    num_cycles = 0
    while tuple(memory) not in states:
        #keep track of when each state was seen
        states[tuple(memory)] = num_cycles
        cycle(memory)
        num_cycles += 1
    cycle_length = num_cycles - states[tuple(memory)]
    return (num_cycles, cycle_length)

M = [0, 2, 7, 0]
#Part 1
assert reallocate(M)[0] == 5
cycle(M)
assert M == [2, 4, 1, 2] 
#Part 2
assert reallocate(M)[1] == 4

memory = [int(i) for i in utils.import_file("Inputs/input6.txt").split()]
num_cycles, cycle_length = reallocate(memory)
print("Part 1: {}".format(num_cycles))
print("Part 2: {}".format(cycle_length))
