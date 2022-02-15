from copy import deepcopy


class Program:
    def __init__(self, data):
        self.data = data
        self.ip = 0
        self.acc = 0
        self.loops = 0

    def parse_line(self):
        return self.data[self.ip].split()

    def tick(self):
        instr, num = self.parse_line()
        if instr == 'acc':
            self.acc += int(num)
            self.ip += 1
        elif instr == 'jmp':
            self.ip += int(num)
        elif instr == 'nop':
            self.ip += 1
        self.loops += 1

    def part1(self):
        seen = set()
        while True:
            if self.ip in seen:
                return self.acc
            seen.add(self.ip)
            self.tick()

    def part2(self):
        while self.loops < 1000:
            if self.ip >= len(self.data):
                return self.acc
            self.tick()


with open('inputs/08.in', 'r') as f:
    data = f.read().splitlines()

# Part1
print('Part1:', Program(data).part1())

# Part2
for i, line in enumerate(data):
    data_copy = deepcopy(data)
    a, b = line.split()
    if a == 'nop':
        data_copy[i] = f'jmp {b}'
    elif a == 'jmp':
        data_copy[i] = f'nop {b}'
    if res := Program(data_copy).part2():
        print('Part2:', res)
        break
