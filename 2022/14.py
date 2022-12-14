with open('inputs/14.in') as f:
    data = [x.strip().split(' -> ') for x in f.readlines()]


placed = set()
for row in data:
    for i in range(len(row)-1):
        cur = row[i]
        nxt = row[i+1]
        cur_x, cur_y = [int(x) for x in cur.split(',')]
        nxt_x, nxt_y = [int(x) for x in nxt.split(',')]
        for rx in range(min([cur_x, nxt_x]), max([cur_x, nxt_x])+1):
            for ry in range(min([cur_y, nxt_y]), max([cur_y, nxt_y])+1):
                placed.add((rx, ry))

max_y = max(r[1] for r in placed) + 2
# bruteforce the floor
for x in range(-999, 1000):
    placed.add((x, max_y))

sand_x = 500
sand_y = 0
sand_settled = 0
while True:
    # down
    if (sand_x, sand_y+1) not in placed:
        sand_y += 1
        continue
    # left
    if (sand_x-1, sand_y+1) not in placed:
        sand_x -= 1
        sand_y += 1
        continue
    # right
    elif (sand_x+1, sand_y+1) not in placed:
        sand_x += 1
        sand_y += 1
        continue

    # settle
    placed.add((sand_x, sand_y))
    sand_settled += 1
    if sand_x == 500 and sand_y == 0:
        break
    sand_x = 500
    sand_y = 0

print(sand_settled)
