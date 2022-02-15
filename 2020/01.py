with open('inputs/01.in', 'r') as f:
    nums = [int(x) for x in f.readlines()]

def sum_2(nums):
    for first in nums:
        for second in nums:
            if first + second == 2020:
                return first * second

def sum_3(nums):
    for first in nums:
        for second in nums:
            for third in nums:
                if first + second + third == 2020:
                    return first * second * third

print(sum_2(nums))
print(sum_3(nums))
