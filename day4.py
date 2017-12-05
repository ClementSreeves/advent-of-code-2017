#!/usr/bin/env python3

import utils
import string


def isValid(passphrase, anagrams=False):
    """Determines whether passphrase is valid.

    Checks whether the given string consists of only lower case letters and
    spaces, and that there are no duplicate words, optionally including
    anagrams.

    Args:
        passphrase: A string representing the passphrase
        anagrams: Boolean that checks for anagrams if True

    Returns:
        Boolean whether or not the passphrase is valid."""
    valid_chars = string.ascii_lowercase + ' '
    for character in passphrase:
        if character not in valid_chars: return False 
    words = passphrase.split()
    if anagrams:
        words = [''.join(sorted(word)) for word in words]
    return len(set(words)) == len(words)

phrases = utils.import_file("Inputs/input4.txt", split=True)

#Part 1
assert isValid("aa bb cc dd ee")
assert (not isValid("aa bb cc dd aa"))
assert isValid("aa bb cc dd aaa")

#Part 2
assert isValid("abcde fghij", True)
assert (not isValid("abcde xyz ecdab", True))
assert isValid("a ab abc abd abf abj", True)
assert isValid("iiii oiii ooii oooi oooo", True)
assert not isValid("oiii ioii iioi iiio", True)

print("Part 1: {}".format(sum(map(isValid, phrases))))
print("Part 2: {}".format(sum([isValid(phrase, True) for phrase in phrases])))
