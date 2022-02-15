import sys
from collections import defaultdict

data = open('input14').read().strip()
data = data.split('\n')

# Parsing
instructions = {}
for line in data:
    components, product = line.split(' => ')
    prod_num, prod_key = product.split(' ')
    prod_num = int(prod_num)
    ingredients = []
    for comp in components.split(', '):
        num, chem = comp.split(' ')
        ingredients.append((int(num), chem))
    instructions[prod_key] = (prod_num, ingredients)

# print('instructions:', instructions)

def produce_fuel(amount):
    need = defaultdict(int, {'FUEL': amount})
    reserve = defaultdict(int)

    answer = 0
    while need:
        need_ingr, need_num = need.popitem()
        cost_increment, components_list = instructions[need_ingr]
        multiplier, remainder = divmod(need_num, cost_increment)
        if remainder:
            reserve[need_ingr] = cost_increment - remainder
            multiplier += 1
        for num_ingr, ingr in components_list:
            # print(reserve)
            if ingr == 'ORE':
                answer += multiplier * num_ingr - reserve[ingr]
            else:
                need[ingr] += multiplier * num_ingr - reserve[ingr]
                del reserve[ingr]

    return answer

print(produce_fuel(1))

fuel_min = 1
fuel_max = 3000000
running = True
while running:
    to_try = (fuel_min + fuel_max) // 2
    produced = produce_fuel(to_try)
    if fuel_max - fuel_min == 1:
        print(to_try)
        break
    if produced > 1000000000000:
        fuel_max = to_try
    else:
        fuel_min = to_try
