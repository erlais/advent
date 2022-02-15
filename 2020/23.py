def run(cups, n_times):
    circle = {inp[i]: inp[(i+1) % len(inp)] for i in range(len(inp))}
    i = cups[0]
    for _ in range(n_times):
        cur_label = i
        nxt = circle[i]
        picked_up = []
        for _ in range(3):
            picked_up.append(nxt)
            nxt = circle[nxt]
        dest = cur_label - 1
        while True:
            if dest < 1:
                dest = max(circle)
            if dest not in picked_up:
                break
            dest -= 1
        circle[cur_label] = circle[picked_up[-1]]
        circle[picked_up[-1]] = circle[dest]
        circle[dest] = picked_up[0]
        i = nxt
    return circle

# Part 1
inp = [int(x) for x in '789465123']
p1_circle = run(inp, 100)
p1 = ''
i = 1
for _ in range(len(inp) - 1):
    nxt = p1_circle[i]
    p1 += str(nxt)
    i = nxt
print('Part1:', p1)

# Part 2
inp = inp + list(range(max(inp)+1, 1000001))
p2_circle = run(inp, int(10000000))
first_cup = p2_circle[1]
print('Part2:', first_cup * p2_circle[first_cup])
