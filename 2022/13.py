import json
from functools import cmp_to_key

with open('inputs/13.in') as f:
    data = [x.strip() for x in f.readlines() if x != '\n']
    data2 = data.copy()


def compare(left, right):
    # print(f'comparing {left} -> {right}')
    if isinstance(left, int):
        if isinstance(right, int):
            return left - right
        elif isinstance(right, list):
            return compare([left], right)
    elif isinstance(left, list):
        if isinstance(right, int):
            return compare(left, [right])
        elif isinstance(right, list):
            for i in range(min(len(left), len(right))):
                res = compare(left[i], right[i])
                if not res == 0:
                    return res
            return compare(len(left), len(right))


i = 1
p1 = []
while data:
    left = json.loads(data.pop(0))
    right = json.loads(data.pop(0))
    if compare(left, right) < 0:
        p1.append(i)
    i += 1
print(sum(p1))


data2.append('[[2]]')
data2.append('[[6]]')
data2 = [json.loads(x) for x in data2]
data2.sort(key=cmp_to_key(compare))
i1 = data2.index([[2]]) + 1
i2 = data2.index([[6]]) + 1
print(i1 * i2)
