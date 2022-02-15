with open('inputs/02.in', 'r') as f:
    in_data = f.readlines()

def parse_row(row):
    parts = row.split()
    ranges = parts[0].split('-')
    return {
        'low': int(ranges[0]),
        'high': int(ranges[1]),
        'policy': parts[1].rstrip(':'),
        'password': parts[2]
    }

def part1(row):
    policy_range = list(range(row['low'], row['high']+1))
    return row['password'].count(row['policy']) in policy_range

def part2(row):
    indx1 = row['password'][row['low']-1] == row['policy']
    indx2 = row['password'][row['high']-1] == row['policy']
    return indx1 ^ indx2

parsed_rows = [parse_row(x) for x in in_data]
print('Part1:', sum(part1(x) for x in parsed_rows))
print('Part2:', sum(part2(x) for x in parsed_rows))
