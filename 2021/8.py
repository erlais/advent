with open('inputs/8.in') as f:
    data = [x.strip() for x in f.readlines()]

# Part 1
part1 = 0
for row in data:
    _, output = row.split(' | ')
    out_words = output.split()
    for word in out_words:
        if len(word) in [2, 4, 3, 7]:  # 1, 4, 7, 8
            part1 += 1
print(part1)

# Part 2
part2 = []
for row in data:
    input, output = row.split(' | ')
    in_words = [sorted(x) for x in input.split()]
    out_words = [sorted(x) for x in output.split()]
    in_words = sorted(in_words, key=len)

    inmap = {
        8: in_words.pop(-1),
        1: in_words.pop(0),
        7: in_words.pop(0),
        4: in_words.pop(0),
    }

    for iw in in_words:
        inter_counts = (
            len(set(inmap[1]) & set(iw)),
            len(set(inmap[7]) & set(iw)),
            len(set(inmap[4]) & set(iw)),
        )
        if len(iw) == 5:
            # 2, 3, 5
            if inter_counts == (1, 2, 2):
                inmap[2] = iw
            elif inter_counts == (2, 3, 3):
                inmap[3] = iw
            elif inter_counts == (1, 2, 3):
                inmap[5] = iw
        elif len(iw) == 6:
            # 0, 6, 9
            if inter_counts == (2, 3, 3):
                inmap[0] = iw
            elif inter_counts == (1, 2, 3):
                inmap[6] = iw
            elif inter_counts == (2, 3, 4):
                inmap[9] = iw

    out_num = ''
    for ow in out_words:
        for k, v in inmap.items():
            if ow == v:
                out_num += str(k)
    part2.append(int(out_num))
print(sum(part2))