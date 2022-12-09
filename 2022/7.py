from collections import defaultdict


with open('inputs/7.in') as f:
    data = [x.strip() for x in f.readlines()]

path = []
ls = False
sizes = defaultdict(int)

for row in data:

    if ls and not row.startswith('$'):
        a, _ = row.split()
        if a == 'dir':
            continue

        tmp = []
        for folder in path:
            tmp.append(folder)
            sizes['/'.join(tmp)] += int(a)

    elif ls and row.startswith('$'):
        ls = False

    if row.startswith('$ cd'):
        cwd = row.split()[-1]
        if cwd == '..':
            path = path[:-1]
        else:
            path.append(cwd)

    elif row.startswith('$ ls'):
        ls = True

print(sum(x for x in sizes.values() if x <= 100000))

available = 70000000 - sizes['/']
to_delete = 30000000 - available

print(min(x for x in sizes.values() if x >= to_delete))
