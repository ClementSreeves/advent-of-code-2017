with open('/storage/emulated/0/qpython/advent-of-code/input11.txt') as f:
    directions = f.read().split(',')

moves = {'n': 2j, 'ne': 1 + 1j, 'nw': -1 + 1j, 's': -2j, 'se': 1 - 1j, 'sw': -1 - 1j}

def steps_home(location):
    h_dist = abs(location.real)
    rem_v_dist = abs(location.imag) - h_dist
    return h_dist + rem_v_dist / 2 if rem_v_dist > 0 else h_dist

def follow(directions):
    loc = complex(0,0)
    for d in directions:
        loc += moves[d]
    return loc
    
def furthest(directions):
    loc = complex(0,0)
    max_dist = 0
    for d in directions:
        loc += moves[d]
        max_dist = max(steps_home(loc), max_dist)
    return max_dist

print(steps_home(follow(directions)))
print(furthest(directions))