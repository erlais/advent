import re
from itertools import product

with open('inputs/14.in', 'r') as f:
    data = f.read().splitlines()

# Part 1
mem = {}
for line in data:
    if line.startswith('mask'):
        mask = line.split()[-1]
    else:
        addr, val = re.search(r'mem\[(\d+)\] = (\d+)', line).groups()
        addr, val = int(addr), bin(int(val))[2:]
        new_val = list(mask)
        for i, num in enumerate(reversed(val)):
            m_id = -i-1
            if mask[m_id] == 'X':
                new_val[m_id] = num
        new_val = ''.join(new_val).lstrip('X').replace('X', '0')
        mem[addr] = int(new_val, 2)
print('Part1:', sum(mem.values()))

# Part 2
mem = {}
for line in data:
    if line.startswith('mask'):
        mask = line.split()[-1]
    else:
        addr, val = re.search(r'mem\[(\d+)\] = (\d+)', line).groups()
        addr, val = bin(int(addr))[2:], int(val)
        new_addr = list(mask)
        for i, num in enumerate(reversed(addr)):
            m_id = -i-1
            if mask[m_id] == '0':
                new_addr[m_id] = num
        new_addr = ''.join(new_addr).lstrip('0')
        combinations = product(*[[1, 0]] * new_addr.count('X'))
        for comb in combinations:
            tmp = new_addr.replace('X', '%s')
            mem[int(tmp % comb, 2)] = val
print('Part2:', sum(mem.values()))
