with open('inputs/9.in') as f:
    data = [x.strip() for x in f.readlines()]

directions = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, -1),
    'D': (0, 1),
}

rope = [(0, 0) for _ in range(10)]
visited = set()

def sign(inpt):
    return -1 if inpt < 0 else 1

def move(h, t):
    dx = h[0] - t[0]
    dy = h[1] - t[1]
    new_x = t[0]
    new_y = t[1]
    if abs(dx) <= 1 and abs(dy) <= 1:
        pass
    elif abs(dx) > 1 and not dy:
        new_x += sign(dx)
    elif abs(dy) > 1 and not dx:
        new_y += sign(dy)
    else:
        new_x += sign(dx)
        new_y += sign(dy)
    return new_x, new_y

for row in data:
    d, amount = row.split()
    for _ in range(int(amount)):
        rope[0] = (rope[0][0] + directions[d][0], rope[0][1] + directions[d][1])
        for idx in range(1, len(rope)):
            rope[idx] = move(rope[idx-1], rope[idx])
        visited.add(rope[-1])

print(len(visited))
