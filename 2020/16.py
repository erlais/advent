import re
from collections import defaultdict
from math import prod

with open('inputs/16.in', 'r') as f:
    data = f.read().strip()
    rules, my, nearby = data.split('\n\n')
    valid = defaultdict(list)
    for rule in rules.splitlines():
        r = re.findall(r'(\d+)-(\d+) or (\d+)-(\d+)', rule)[0]
        r = list(map(int, r))
        key = rule.split(':')[0]
        valid[key].extend(list(range(r[0], r[1]+1)))
        valid[key].extend(list(range(r[2], r[3]+1)))
    all_ranges = sum(valid.values(), [])

# Part 1
new_nearby = []
invalid = []
for near in nearby.splitlines()[1:]:
    values = [int(x) for x in near.split(',')]
    bad_values = [x for x in values if x not in all_ranges]
    if not bad_values:
        new_nearby.append(near)
    invalid.extend(bad_values)
print('Part1:', sum(invalid))

# Part 2
transposed = defaultdict(list)
for ticket in new_nearby:
    fields = map(int, ticket.split(','))
    for i, fld in enumerate(list(fields)):
        transposed[i].append(fld)

seen = {}
while valid:
    for field_idx, nearby_vals in transposed.items():
        fits = []
        for rule_name, rule_range in valid.items():
            if set(nearby_vals).issubset(set(rule_range)):
                fits.append(rule_name)
        if len(fits) == 1:  # values fit into ONLY one rule
            seen[fits[0]] = field_idx
            del valid[fits[0]]

p2 = []
my_fields = [int(x) for x in my.splitlines()[1].split(',')]
for k, v in seen.items():
    if k.startswith('departure'):
        p2.append(my_fields[v])
print('Part2:', prod(p2))
