with open('inputs/13.in', 'r') as f:
    data = f.read().splitlines()
    sched = data[1].split(',')

# Part1
res = []
for bus in sched:
    if bus == 'x':
        continue
    bus = int(bus)
    depart = 0
    while depart <= int(data[0]):
        depart += bus
    res.append((depart, bus))

to_wait = min(res)[0] - int(data[0])
print('Part1:', to_wait * min(res)[1])


# Part2
lcm = 1
i = 0
for bus in sched:
    if bus == 'x':
        i += 1
        continue
    bus = int(bus)
    while i % bus != 0:
        i += lcm
    lcm *= bus
    i += 1

print('Part2:', i - len(sched))
