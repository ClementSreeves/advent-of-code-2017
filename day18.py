import utils
from collections import defaultdict

def quantify(val, registers):
    try:
        return int(val) 
    except ValueError:
        return registers[val]

def run(instructions):
    registers = defaultdict(int)
    i = 0
    while 0 <= i <= len(instructions):
        command, *arguments = instructions[i].split()
        if len(arguments) == 1:
            X = quantify(arguments[0], registers)
        elif command == 'jgz':
            X, Y = [quantify(val, registers) for val in arguments]
            if X > 0: 
                i += Y
                continue
        else:
            X, Y = [arguments[0], quantify(arguments[1], registers)]
        #execute the command    
        if command == 'snd':
            snd(X, registers)
        elif command == 'set':
            setval(X, Y, registers)
        elif command == 'add':
            add(X, Y, registers)
        elif command == 'mul':
            mul(X, Y, registers)
        elif command == 'mod':
            mod(X, Y, registers)
        elif command == 'rcv':
            if rcv(X, registers): 
                print("Value was {}".format(rcv(X, registers)))
                break
        #increment
        i += 1

def snd(X, registers):
    registers['snd'] = X

def setval(X, Y, registers):
    registers[X] = Y

def add(X, Y, registers):
    registers[X] += Y

def mul(X, Y, registers):
    registers[X] *= Y

def mod(X, Y, registers):
    registers[X] %= Y

def rcv(X, registers):
    return registers['snd'] if X else None

instructions = utils.import_file("Inputs/input18.txt", split=True)
run(instructions)
