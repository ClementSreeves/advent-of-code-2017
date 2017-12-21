import re
import sys

def process(line):
    match = re.match(r'(?P<name>\w+) \((?P<weight>\d+)\)( -> (?P<children>.*))?', line)
    output = match.groupdict()
    output['weight'] = int(output['weight'])
    if output['children']:
        output['children'] = output['children'].split(', ')
    return output

with open('/storage/emulated/0/qpython/advent-of-code/input7.txt') as f:
    lines = [line.strip() for line in f.readlines()]

program_dict = {}
while lines:
    new_lines = []
    for line in lines:
        p = process(line)
        if p['children']:
            try:
                p['children'] = [program_dict[x] for x in p['children']]
                program_dict[p['name']] = p
            except KeyError:
                new_lines.append(line)
        else:
            program_dict[p['name']] = p
    lines = new_lines
    if len(lines) < 10: print(lines)

def calculate_weight(disk):
    if disk['children']:
        subtower_weights = [calculate_weight(child) for child in disk['children']]
        if max(subtower_weights) != min(subtower_weights):
            print([(disk['children'][i]['name'], disk['children'][i]['weight'], subtower_weights[i]) for i in range(len(subtower_weights))])
            sys.exit()
        else:
            return disk['weight'] + sum(subtower_weights)
    else:
        return disk['weight']
        
tower = program_dict['cqmvs']
calculate_weight(tower)

