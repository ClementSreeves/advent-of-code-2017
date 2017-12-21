import string

def swap_elems(l, ind1, ind2):
    p1, p2 = (l[ind1], l[ind2])
    l[ind1] = p2
    l[ind2] = p1

def dance(programs, moves):
    for move in moves:
        if move[0] == 's':
            n = int(move[1:])
            programs = programs[-n:] + programs[:-n]
        elif move[0] == 'x':
            index1, index2 = [int(i) for i in move[1:].split('/')]
            swap_elems(programs, index1, index2)
        elif move [0] == 'p':
            index1, index2 = (programs.index(move[1]), programs.index(move[3]))
            swap_elems(programs, index1, index2)
        else:
            print('unknown move')
            break
    return programs
    
def calculate_cycles(programs, moves):
    cycles = {}
    initial_config = programs
    permutation = dance(initial_config, moves)
    for p in initial_config:
        cycle = []    
        current_val = p
        while current_val != p or len(cycle) == 0:
            cycle.append(current_val)
            index = initial_config.index(current_val)
            current_val = permutation[index]
        cycles[p] = cycle
    return cycles
    
programs = list(string.ascii_lowercase[:16])

with open("/storage/emulated/0/qpython/advent-of-code/input16.txt") as f:
    moves = f.read().strip().split(',')
#moves = ['s1', 'x3/4', 'pe/b']
programs1= dance(programs, moves)
print(''.join(programs1))

cycles = calculate_cycles(programs, moves)

n = 1000000000
result = []
for p in programs:
    cycle = cycles[p]
    result.append(cycle[n % len(cycle)])
print(''.join(result))
    
