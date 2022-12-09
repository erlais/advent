with open('inputs/2.in') as f:
    data = [x.strip()
            .replace('X', 'A')
            .replace('Y', 'B')
            .replace('Z', 'C')
            for x in f.readlines()]

win = {
    'A': ('C', 1),
    'B': ('A', 2),
    'C': ('B', 3),
}

part1 = 0
for row in data:
    opp, me = row.split(' ')
    if me == opp:
        part1 += 3 + win[me][1]
    elif win[me][0] == opp:
        part1 += 6 + win[me][1]
    else:
        part1 += win[me][1]
print(part1)

part2 = 0
for row in data:
    opp, res = row.split(' ')
    if res == 'A':
        tmp = win[opp][0]
        part2 += win[tmp][1]
    elif res == 'B':
        part2 += 3 + win[opp][1]
    else:
        for target, scr in win.values():
            if target == opp:
                part2 += 6 + scr
                break
print(part2)
