import re

def strip_deletions(s):
    while re.search(r'!.', s):
        s = re.sub(r'!.', '', s)
    return s
    
def strip_garbage(s):
    garbage_pattern = r'<[^>]*>'
    garbage_count = 0
    while True:    
        match = re.search(garbage_pattern, s)
        if match:
            s = re.sub(garbage_pattern, '', s, count=1)
            garbage_count += len(match.group()) - 2
        else:
            break
    return (s, garbage_count)
    
def brace_score(s):
    score = 0
    value = 0
    for brace in s:
        if brace == '{':
            value += 1
        if brace == '}':
            score += value
            value -= 1
    return score

with open("/storage/emulated/0/qpython/advent-of-code/input9.txt") as f:
    stream = f.read()
print(brace_score(strip_garbage(strip_deletions(stream))[0]))
print(strip_garbage(strip_deletions(stream))[1])
print(strip_deletions('{<!!!>>}'))

print(strip_garbage(strip_deletions('{{<a>},{<!>},{<!>},{<a>}}')))

print(brace_score('{}'))
print(brace_score('{{{}}}'))
print(brace_score('{{}{}}'))
print(brace_score('{{{}{}{{}}}}'))