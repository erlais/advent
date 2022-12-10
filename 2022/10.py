with open('inputs/10.in') as f:
    data = [x.strip() for x in f.readlines()]

X = 1
action = 0
p1 = []
p2 = []
for cycle in range(1, 241):
    sprite = [X-1, X, X+1]
    if (cycle - 1) % 40 in sprite:
        p2.append('#')
    else:
        p2.append(' ')

    if cycle in [20, 60, 100, 140, 180, 220]:
        p1.append(cycle * X)

    if not action:
        instr = data.pop(0)
        if instr == 'noop':
            continue
        action = int(instr.split()[1])
    else:
        X += action
        action = 0

print(sum(p1))

line = []
for i, px in enumerate(p2):
    line.append(px)
    if len(line) == 40:
        print(''.join(line))
        line = []
