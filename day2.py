import utils
import itertools

def checksum(matrix):
    return sum([(max(row) - min(row)) for row in matrix])

def even_divisor(l):
    for combo in itertools.combinations(l, 2):
        low, high = sorted(combo)
        q, r = divmod(high, low)
        if r == 0: return q
        
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
