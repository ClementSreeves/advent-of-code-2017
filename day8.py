from collections import defaultdict
import re

def process(instructions):
    registers = defaultdict(int)
    current_max = 0
    for instruction in instructions:
        match = re.match(r'(?P<reg>\w+) (?P<op>\w+) (?P<val>[-\d]+) if (?P<reg2>\w+)(?P<end>.+)', instruction)
        if eval('registers["' + match.group('reg2') + '"]' + match.group('end')):
            multiplier = -1 if (match.group('op') == 'dec') else 1
            registers[match.group('reg')] += multiplier * int(match.group('val'))
            new_val = registers[match.group('reg')]
            current_max = max(current_max, new_val)
#    return max(registers.items(), key=lambda x: x[1])
    return current_max
    
with open('storage/emulated/0/qpython/advent-of-code/input8.txt') as f:
    instructions = [line.strip() for line in f.readlines()]
print(process(instructions))
