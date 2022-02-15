from collections import deque

data = '7,12,1,0,16,2'
nums = deque([int(x) for x in data.split(',')])

def get_nth(nth):
    i = 0
    seen = {}
    while i < nth-1:
        num = nums.popleft()
        if nums:  # initial numbers
            seen[num] = i
            i += 1
            continue
        if num not in seen.keys():
            nums.append(0)
        else:
            diff = (i+1) - (seen[num]+1)
            nums.append(diff)
        seen[num] = i
        i += 1
    return diff

print('Part1': get_nth(2020))
print('Part2': get_nth(30000000))
