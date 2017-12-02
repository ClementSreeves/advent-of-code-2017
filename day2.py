#!/usr/bin/env python3

import utils
import itertools

class InvalidInputError(Exception):
    pass

def checksum(matrix):
    return sum([(max(row) - min(row)) for row in matrix])

def even_divisor(l):
    """Finds the quotient of the two numbers where one divides the other.

    Assumes that there are only two numbers where one divides the other. Finds
    those numbers, and returns their quotient.

    Args:
        l: A list of integers

    Returns:
        An integer quotient of the two numbers found

    Raises:
        InvalidInputError: The list did not contain two numbers where one
                           evenly divides the other
    """
    for combo in itertools.combinations(l, 2):
        low, high = sorted(combo)
        q, r = divmod(high, low)
        if r == 0: return q
    raise InvalidInputError("The list did not contain two numbers where one"
                              " evenly divides the other")    

def divsum(matrix):
    return sum([even_divisor(row) for row in matrix])

#part 1
assert checksum([[5, 1, 9, 5],
                 [7, 5, 3],
                 [2, 4, 6, 8]]) == 18

#part 2
assert divsum([[5, 9, 2, 8],
               [9, 4, 7, 3],
               [3, 8, 6, 5]]) == 9

input_file = utils.import_file("Inputs/input2.txt")

matrix = []
for row in input_file.split('\n'):
    matrix.append([int(entry) for entry in row.split('\t')])

print("Part 1: {}".format(checksum(matrix)))
print("Part 2: {}".format(divsum(matrix)))
