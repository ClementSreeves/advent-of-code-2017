#!/usr/bin/env python3

import utils

def solve_captcha(s, shift=1):
    """Finds the sum of the digits that match a shifted number of digits ahead.

    The captcha requires you to review a sequence of digits (your puzzle
    input) and find the sum of all digits that match the digit a certain 
    number of digits ahead in the list. The list is circular, so the digit
    after the last digit is the first digit in the list.

    Args:
        s: A string of the captcha digits of length at least 2.
        shift: An integer number of digits ahead to look for a match. 

    Returns:
        An integer solution to the captcha.
    """
    shifted = s[shift:] + s[0:shift]
    return sum([int(s[i]) for i in range(len(s)) if s[i] == shifted[i]])

#part 1
assert (solve_captcha("1122") == 3)
assert (solve_captcha("1111") == 4)
assert (solve_captcha("1234") == 0)
assert (solve_captcha("91212129") == 9)

#part 2
assert (solve_captcha("1212", shift=2) == 6)
assert (solve_captcha("1221", shift=2) == 0)
assert (solve_captcha("123425", shift=3) == 4)
assert (solve_captcha("123123", shift=3) == 12)
assert (solve_captcha("12131415", shift=4) == 4)

s = utils.import_file("Inputs/input-1-1.txt")

print("Part 1: {}".format(solve_captcha(s)))
print("Part 2: {}".format(solve_captcha(s, shift=len(s)//2)))
