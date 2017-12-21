def generator(factor, seed, multiple=1, divisor=2147483647):
    previous = seed
    while True:
        previous = previous * factor % divisor
        if previous % multiple == 0: yield previous

def match_values(seedA, seedB, factorA=16807, factorB=48271, trials=40000000, verbose=False):
    genA = generator(factorA, seedA, multiple=4)
    genB = generator(factorB, seedB, multiple=8)
    score = 0
    for _ in range(trials):
        nextA = bin(next(genA))[-16:]
        nextB = bin(next(genB))[-16:]
        #if verbose: print('A: {} B: {}'.format(nextA, nextB))
        if nextA == nextB:
            score += 1
    return score
    
print(match_values(873, 583, trials=5000000))
