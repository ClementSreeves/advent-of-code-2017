def rotations(pattern):
    result = []
    for _ in range(3):
        result.append(list(zip(*[reversed(t) for t in test])))
    return zip(*pattern)
