with open('inputs/6.in') as f:
    data = f.read().strip()

mark_len = 14

for i in range(len(data)):
    marker = data[i:i+mark_len]
    if len(set(marker)) == mark_len:
        print(i+mark_len)
        break
