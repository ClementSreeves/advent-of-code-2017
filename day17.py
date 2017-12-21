def spinlock(step_size, iterations=2017, verbose=False):
    circular_buffer = [0]
    index = 0
    current_val = None
    for i in range(1, iterations + 1):
        index = ((index + step_size) % i) + 1
        if index == 1: current_val = i
    return current_val

print(spinlock(359, iterations=50000000))


