data = open('input2').read().strip().split()

# Part 1
twos = 0
threes = 0
for row in data:
    got2 = False
    got3 = False
    for char in row:
        cnt = row.count(char)
        if row.count(char) == 2 and not got2:
            twos += 1
            got2 = True
        if row.count(char) == 3 and not got3:
            threes += 1
            got3 = True
print(twos * threes)

# Part 2
seen = set()
for a in data:
    for b in data:
        diff = [0, 0]
        if a == b or b in seen:
            continue
        for i in range(len(a)):
            if a[i] != b[i]:
                diff[0] += 1
                diff[1] = i  # pos of changed character
        if diff[0] == 1:
            bad = diff[1]
            print(a[:bad] + a[bad+1:])
        seen.add(a)
