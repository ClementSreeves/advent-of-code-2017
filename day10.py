with open("/storage/emulated/0/qpython/advent-of-code/input10.txt") as f:
    my_input = bytes(f.read().strip(), encoding='ascii')

def rotate(array, amount):
    for _ in range(abs(amount)):
        if amount > 0:
            array.insert(0, array.pop())
        else:
            array.append(array.pop(0))
    return array
    
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

#print(xor([65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22]))

def knot_hash(b):
    b = b + bytes([17, 31, 73, 47, 23])
    length_array = list(b)
    array = list(range(256)) 
    index = skip = 0
    for _ in range(64):
        array, index, skip = process(array, length_array, index=index, skip=skip)
    chunks = [array[n:n+16] for n in range(0, len(array), 16)]
    dense_hash = ''.join([format(xor(chunk), '02x') for chunk in chunks])
    return dense_hash

print(knot_hash(my_input))