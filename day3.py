#!/usr/bin/env python3

import math

neighbours = N, E, S, W, NW, NW, SW, SE = (1j, 1, -1j, -1, 1j-1, 1j+1, -1j-1,
                                           -1j+1)

def find_neighbours(point):
    """Returns the complex points neighbouring the given point"""
    return map(lambda x: x + point, neighbours)

def sum_of_neighbours(point, location_values):
    """Calculates the sum of the values of neighouring points""" 
    sum = 0
    for neighbour in find_neighbours(point):
        try: sum += location_values[neighbour]
        except KeyError: pass
    return sum

def spiral_location_generator():
    """Generates consecutive points representing locations in spiral memory"""
    direction = E
    location = complex(0,0)
    steps_until_turn = 1
    turns = 0
    while True:
        for i in range(steps_until_turn):
            yield location
            location += direction
        direction *= N
        turns += 1
        if turns % 2 == 0: steps_until_turn += 1

def neighbour_sum_spiral_generator():
    """Generates consecutive values in the sum spiral"""
    location_generator = spiral_location_generator()
    location_values = {}
    while True:
        location = next(location_generator)
        value = sum_of_neighbours(location, location_values) or 1
        yield value
        location_values[location] = value

def spiral_address_location(address):
    """Finds location on the complex plane for a given spiral address"""
    gen = spiral_location_generator()
    for i in range(address):
        loc = next(gen)
    return loc

def taxicab_distance(point):
    return abs(point.imag) + abs(point.real)

#Below is my original solution to Part 1. It is better computationally for
#large addresses but is far less readable.

#The numbers on the segment defined by x = -y, x >= 0 are the odd squares,
#since each spiral finishes in the bottom right hand corner.

def spiral_address_location2(address):
    """Finds location on the complex plane for a given spiral address."""

    root_ceil = math.ceil(math.sqrt(address))
    root_odd_ceil = root_ceil if root_ceil % 2 else root_ceil + 1
    #spiral depth starting at 0
    depth = (root_odd_ceil - 1) // 2
    corner_value = root_odd_ceil ** 2
    location = complex(depth, -depth)
    direction = W
    distance = corner_value - address
    for i in range(distance):
        location += direction
        if (i + 1) % (root_odd_ceil - 1) == 0:
            direction *= S
    return location

 
assert taxicab_distance(2 - 3j) == 5

assert taxicab_distance(spiral_address_location(1)) == 0
assert taxicab_distance(spiral_address_location(12)) == 3 
assert taxicab_distance(spiral_address_location(23)) == 2 
assert taxicab_distance(spiral_address_location(1024)) == 31 

my_input = 347991
print("Part 1: {}".format(taxicab_distance(spiral_address_location(my_input))))

gen = neighbour_sum_spiral_generator()
while True:
    value = next(gen)
    if value > my_input:
        print("Part 2: {}".format(value))
        break
