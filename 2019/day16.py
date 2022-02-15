from copy import copy
import itertools
from datetime import datetime

DATA = open('input16').read().strip()

offset = int(DATA[:7])

DATA = DATA * 10000
DATA = DATA[offset:]
DATA = [int(x) for x in DATA]

pattern = [0, 1, 0, -1]

def get_phase_pattern(phase, ptrn_list):
    new_list = [[x] * (1+phase) for x in ptrn_list]
    res = []
    for item in new_list:
        res += item
    return res


def do_phase_p1(data):
    new_data = []
    for phase, digit in enumerate(data):
        phase_pattern = get_phase_pattern(phase, pattern)
        new_digit = 0
        for i, DIGIT in enumerate(data):
            new_digit += DIGIT * phase_pattern[(i+1) % len(phase_pattern)]
        new_digit = abs(new_digit) % 10
        new_data.append(new_digit)
    return new_data

def do_phase_p2(data):
    # because offset is so big, phase is always 1
    part_sum = 0
    for i in range(len(data)-1, -1, -1):
        part_sum += data[i]
        data[i] = part_sum % 10
    return data

i = 0
data = copy(DATA)
while i < 100:
    # data = do_phase_p1(data)
    data = do_phase_p2(data)
    i += 1

answer = [str(x) for x in data]
print(''.join(answer[:8]))
