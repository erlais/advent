# Part 1
with open('inputs/2.in') as f:
    data = [x.strip() for x in f.readlines()]

X = 0
Z = 0

for cmd in data:
    direction, value = cmd.split()
    value = int(value)
    if direction == 'forward':
        X += value
    elif direction == 'down':
        Z += value
    elif direction == 'up':
        Z -= value
print(X * Z)


#Part 2
with open('2.in', 'r') as f:
    data = [x.strip() for x in f.readlines()]

X = 0
Z = 0
AIM = 0

for cmd in data:
    direction, value = cmd.split()
    value = int(value)
    if direction == 'forward':
        X += value
        Z += AIM * value
    elif direction == 'down':
        AIM += value
    elif direction == 'up':
        AIM -= value
print(X * Z)
