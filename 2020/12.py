with open('inputs/12.in', 'r') as f:
    data = f.read().splitlines()

# Part 1
X = Y = 0
dr = 0  # 0 degrees = east
for line in data:
    instr = line[0]
    amount = int(line[1:])
    if instr == 'F':
        if dr == 0:
            X += amount
        elif dr == 90:
            Y -= amount
        elif dr == 180:
            X -= amount
        elif dr == 270:
            Y += amount
    elif instr == 'L':
        dr = (dr - amount) % 360
    elif instr == 'R':
        dr = (dr + amount) % 360
    elif instr == 'N':
        Y += amount
    elif instr == 'S':
        Y -= amount
    elif instr == 'E':
        X += amount
    elif instr == 'W':
        X -= amount
print('Part1:', abs(X) + abs(Y))

# Part 2
def rotate(instr, x, y):
    return (y, -x) if instr == 'R' else (-y, x)

X = 10
Y = 1
shipX = shipY = 0
dr = 0
for line in data:
    instr = line[0]
    amount = int(line[1:])
    if instr == 'F':
        shipX += X * amount
        shipY += Y * amount
    elif instr in ['L', 'R']:
        for _ in range(int(amount/90)):
            X, Y = rotate(instr, X, Y)
    elif instr == 'N':
        Y += amount
    elif instr == 'S':
        Y -= amount
    elif instr == 'E':
        X += amount
    elif instr == 'W':
        X -= amount
print('Part2:', abs(shipX) + abs(shipY))
