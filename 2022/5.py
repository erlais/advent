import re
from collections import defaultdict

with open('inputs/5.in') as f:
    data = f.readlines()

data1 = []
for row in data:
    if row.strip() == '':
        break
    data1.append(row.rstrip())

data2 = [x.strip() for x in data if x.startswith('move')]

stacks = defaultdict(list)
for col, char in enumerate(data1[-1]):
    if char != ' ':
        for i in range(2, len(data1)+1):
            try:
                crate = data1[-i][col]
                if crate != ' ':
                    stacks[char].append(crate)
            except IndexError:
                continue

for row in data2:
    qty, frm, to = re.findall('\d+', row)
    crates = []
    for _ in range(int(qty)):
        if not stacks[frm]:
            continue
        crates.append(stacks[frm].pop(-1))
    # for part1 uncomment reversed
    crates = reversed(crates)
    stacks[to].extend(crates)

res = [x[-1] for x in stacks.values()]
print(''.join(res))

