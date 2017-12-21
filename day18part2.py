import utils
from collections import defaultdict
import time
import threading

def quantify(val, registers):
    try:
        return int(val) 
    except ValueError:
        return registers[val]

class ProgramThread(threading.Thread):
    def __init__(self, program):
        threading.Thread.__init__(self)
        self.program = program

    def run(self):
        self.program.run()

class Program(object):
    def __init__(self, number, instructions, target=None):
        self.number = number
        self.instructions = instructions
        self.registers = defaultdict(int)
        self.registers['p'] = self.number
        self.receiver = self.receive()
        self.receiver.send(None)
        self.message_queue = []
        self.target = target
        self.sent = 0

    def set_target(self, target):
        self.target = target

    def send(self, value):
        #print("Program {} sending a value...".format(self.number))
        self.sent += 1
        self.target.receiver.send(value)
        
    def receive(self):
        while True:
            val = (yield)
            #print("Program {} receiving a value...".format(self.number))
            self.message_queue.append(val)

    def run(self):
        self.i = 0
        while 0 <= self.i < len(self.instructions):
            command, *arguments = self.instructions[self.i].split()
            print(command, *arguments)
            if len(arguments) == 1:
                self.X = quantify(arguments[0], self.registers)
            elif command == 'jgz':
                self.X, self.Y = [quantify(val, self.registers) for val in arguments]
                if self.X > 0: 
                    self.i += self.Y
                    continue
            else:
                self.X, self.Y = [arguments[0], quantify(arguments[1], self.registers)]
            #execute the command
            if command == 'snd':
                self.send(self.X)
            elif command == 'rcv':
                attempts = 0
                while len(self.message_queue) == 0 and attempts < 10:
                    #print("Program {} is waiting...".format(self.number))
                    attempts += 1
                    time.sleep(1)
                if attempts >= 10: break
                print("P {} using {}".format(self.number,
                      self.message_queue[0]))
                self.registers[self.X] = self.message_queue.pop(0)    
            elif command == 'set':
                self.registers[self.X] = self.Y
            elif command == 'add':
                self.registers[self.X] += self.Y
            elif command == 'mul':
                self.registers[self.X] *= self.Y
            elif command == 'mod':
                self.registers[self.X] %= self.Y
            #increment
            self.i += 1

instructions = utils.import_file("Inputs/input18.txt", split=True)
i1 = instructions[:]
i2 = instructions[:]
p1 = Program(0, i1)
p2 = Program(1, i2 , target=p1)
p1.set_target(p2)

thread1 = ProgramThread(p1)
thread2 = ProgramThread(p2)
thread1.start()
thread2.start()

threads = []
threads.append(thread1)
threads.append(thread2)
for t in threads:
    t.join()
print("Part 2: {}".format(p2.sent))


