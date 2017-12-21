with open('/storage/emulated/0/qpython/advent-of-code/input13.txt') as f:
    lines = [line.strip().split(': ') for line in f.readlines()]
config = {int(d): int(r) for d, r in lines}

def severity_score(config, delay=0):
    num_levels = max(config.keys()) + 1
    severity = 0
    for level in range(num_levels):
        if level in config:
            position = level + delay
            caught = position % ((config[level] - 1) * 2) == 0
            if caught: severity += level * config[level]
    return severity

def is_caught(config, delay=0):
    num_levels = max(config.keys()) + 1
    severity = 0
    for level in range(num_levels):
        if level in config:
            position = level + delay
            caught = position % ((config[level] - 1) * 2) == 0
            if caught: return True
    return False
    
delay = 0
while is_caught(config, delay=delay):
    delay += 1
print(delay)