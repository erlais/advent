from collections import defaultdict, deque

with open('inputs/10.in', 'r') as f:
    data = sorted([int(x) for x in f.read().splitlines()])
    data.insert(0, 0)
    data.append(data[-1] + 3)

i = 0
diffs = defaultdict(int)
for line in data:
    diffs[line-i] += 1
    i = line
print('Part1:', diffs[1] * diffs[3])

crumbs = defaultdict(int)
crumbs[data.pop(0)] = 1
for line in data:
    for i in range(1, 4):
        if crumbs.get(line-i):
            crumbs[line] += crumbs[line-i]
print('Part2:', max(crumbs.values()))
