import base64
import itertools

def rotate2(array, amount):
    for _ in range(abs(amount)):
        if amount > 0:
            array.insert(0, array.pop())
        else:
            array.append(array.pop(0))
    return array

def rotate(array, amount):
    amount = amount % 256
    return array[-amount:] + array[:-amount]
    
def process(array, inputs, index=0, skip=0):
    rotation = 0
    for inp in inputs:
        array = rotate(array, index * -1)
        rotation += (index * -1)
        array[:inp] = reversed(array[:inp])
        index = inp + skip
        skip += 1
    array = rotate(array, rotation * -1)
    index = (index - rotation) % len(array)
    return (array, index, skip)

def xor(int_list):
    result = 0
    for i in int_list:
        result = result ^ i
    return result

def knot_hash(b):
    b = b + bytes([17, 31, 73, 47, 23])
    length_array = list(b)
    array = list(range(256)) 
    index = skip = 0
    for _ in range(64):
        array, index, skip = process(array, length_array, index=index, skip=skip)
    chunks = [array[n:n+16] for n in range(0, len(array), 16)]
    dense_hash = bytes([xor(chunk) for chunk in chunks])
    return dense_hash

def bitcount(b):
    count = 0
    while b:
        b &= (b-1)
        count += 1
    return count
    
def used_squares(key, grid_size=128):
    used = 0
    for i in range(grid_size):
        print(i)
        hash_output = knot_hash(bytes(key + '-' + str(i), encoding='utf8'))
        used += sum([bitcount(b) for b in hash_output])
    return used
    
def make_grid(key, grid_size=128):
    grid = []
    for i in range(grid_size):
        hash_output = knot_hash(bytes(key + '-' + str(i), encoding='utf8'))
        bits = ''.join([format(b, '08b') for b in hash_output])
        grid.append([bit == '1' for bit in bits])
    return grid

def expand(point, grid, examined):
    if max(point) >= len(grid) or min(point) < 0:
        return 0
    if grid[point[0]][point[1]] and point not in examined:
        examined.add(point)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        neighbours = [(point[0] + d[0], point[1] + d[1]) for d in directions]
        for neighbour in neighbours:
            expand(neighbour, grid, examined)
        return 1
    else:
        return 0

def regions(grid):
    grid_size = len(grid)
    examined = set([])
    num_regions = 0
    for i, j in itertools.product(range(grid_size), repeat=2):
        num_regions += expand((i,j), grid, examined)
    return num_regions    
       

test_grid = [[1,1,0,2,0,3,0,0],[0,1,0,2,0,3,0,4]]
grid = make_grid('uugsqrei')
print(regions(grid))
