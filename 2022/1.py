calories = []
with open('inputs/1.in') as f:
    elf = 0
    for row in f.readlines():
        row = row.strip()
        if not row:
            calories.append(elf)
            elf = 0
            continue
        elf += int(row)

print(max(calories))
print(sum(sorted(calories)[-3:]))
