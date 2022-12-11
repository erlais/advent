data = open('input1').readlines()
data = [int(x) for x in data]

# Part 1
fuel_sum = sum(int(x / 3) - 2 for x in data)
print(fuel_sum)  # 3380731

# Part 2
def fuel_rec(module, total=0):
    fuel = int(module / 3) - 2
    if fuel <= 0:
        return total
    total += fuel
    return fuel_rec(fuel, total)

res = sum(fuel_rec(x) for x in data)
print(res)  # 5068210
