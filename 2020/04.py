import re

with open('inputs/04.in', 'r') as f:
    rows = f.read().splitlines()

doc_list = []
doc = {}
for i, row in enumerate(rows):
    if row == '':
        doc_list.append(doc)
        doc = {}
    kv_pairs = row.split()
    for pair in kv_pairs:
        k, v = pair.split(':')
        doc[k] = v
    
def is_valid1(doc):
    num_attrs = len(doc.values())
    return num_attrs == 8 or (num_attrs == 7 and not doc.get('cid'))

def is_valid2(doc):
    hgt, hgt_unit = re.search(r'(\d+)(\w+)', doc['hgt']).groups()
    validations = [
        1920 <= int(doc['byr']) <= 2002,
        2010 <= int(doc['iyr']) <= 2020,
        2020 <= int(doc['eyr']) <= 2030,
        (150 <= int(hgt) <= 193 and hgt_unit == 'cm') or (59 <= int(hgt) <= 76 and hgt_unit == 'in'),
        re.match(r'^#[0-9a-f]{6}', doc['hcl']),
        doc['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
        len(doc['pid']) == 9
    ]
    return all(validations)


res1 = [x for x in doc_list if is_valid1(x)]
res2 = [x for x in res1 if is_valid2(x)]
print('Part1:', len(res1))
print('Part2:', len(res2))
