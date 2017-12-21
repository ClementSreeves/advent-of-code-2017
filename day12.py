import re

def find_connected(node, connections, group=None):
    if group is None:
        group = []
    group.append(node)
    [find_connected(i, connections, group=group) for i in connections[node] if i not in group]
    return group
    
with open("/storage/emulated/0/qpython/advent-of-code/input12.txt") as f:
    lines = [line.strip() for line in f.readlines()]

connections = {o: n for o, *n in map(lambda x: re.findall(r'\d+', x), lines)}

print(len(find_connected('0', connections)))

groups = []
seen = set()
for i in range(len(lines)):
    if str(i) not in seen:
        group = find_connected(str(i), connections)
        groups.append(group)
        seen.update(set(group))
#groups = set(all)
print(len(groups))