import copy
import string

data = open('input5').read().strip()


def run(inpt):
    res = []
    for c in inpt:
        if len(res) > 0 and c.lower() == res[-1].lower() and c != res[-1]:
            res.pop()
        else:
            res.append(c)
    return res

ans = []
for letter in string.ascii_lowercase:
    d = copy.copy(data)
    d = d.replace(letter, '').replace(letter.upper(), '')
    ans.append((len(run(d)), letter))

print(min(ans))
