#!/usr/bin/env python3

import utils

def num_jumps(instruction_list, strange_offsets=False):
    """Calculates the number of jumps taken to exit the instruction list.

    Args:
        instruction_list: List of integers representing the instructions.
        strange_offsets: Boolean to set whether the negative offsets are used.

    Returns:
        An integer of the number of steps taken
    """
    #create a copy to avoid modifying the original list
    instruction_list = instruction_list[:]
    list_length = len(instruction_list)
    index = 0
    jumps = 0
    while True:
        if (index < 0) or (index >= list_length):
            return jumps
        else:
            step = instruction_list[index]
            change = -1 if (step > 2 and strange_offsets) else 1
            instruction_list[index] += change 
            index += step
            jumps += 1

#Part 1
assert num_jumps([0, 3, 0, 1, -3]) == 5

#Part 2
assert num_jumps([0, 3, 0, 1, -3], strange_offsets=True) == 10

instructions = [int(n) for n in utils.import_file("Inputs/input5.txt",
                                                  split=True)]
print("Part 1: {}".format(num_jumps(instructions)))
print("Part 2: {}".format(num_jumps(instructions, strange_offsets=True)))
