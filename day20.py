import utils
import re
import itertools

class Particle(object):
    def __init__(self, position, velocity, acceleration):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration

    def step(self):
        self.velocity = [self.velocity[i] + self.acceleration[i] 
                         for i in range(len(self.velocity))]
        self.position = [self.position[i] + self.velocity[i] 
                         for i in range(len(self.position))]

    def distance(self):
        return sum([abs(i) for i in self.position])
        
    def get_position(self):
        return self.position

inputs = utils.import_file("Inputs/input20.txt", split=True)
particles = []
for line in inputs:
    values = [s.split(',') for s in re.findall(r'<(.*?)>', line)]
    pos, vel, acc = [list(map(int, v)) for v in values]
    particles.append(Particle(pos, vel, acc))

for i in range(1000):
    [p.step() for p in particles]
    by_position = lambda x: x.get_position()
    particles = sorted(particles, key=by_position)
    for key, group in itertools.groupby(particles, key=by_position):
        if len(list(group)) > 1:
           particles = list(filter(lambda x: x.get_position() != key,
                                   particles)) 

print("Part 2: {}".format(len(particles)))
#print(sorted([(p.distance(), i) for i, p in enumerate(particles)])[:3])
