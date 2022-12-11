in_data = open('input6').read().splitlines()

data = {}
for rel in in_data:
    p1, p2 = rel.split(')')
    if p1 not in data.keys():
        data[p1] = []
    data[p1].append(p2)

def find(qry, path=False):
    if not path:
        path = []
    for k, v in data.items():
        if qry in v:
            path.append(qry)
            find(k, path)
    return path

found = find('YOU') + find('SAN')
res = [f for f in found if found.count(f) <= 1]
print(len(res)-2)
