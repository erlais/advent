with open('inputs/05.in', 'r') as f:
    data = [x.strip() for x in f.readlines()]

def search(row, high, low=0):
    for char in row:
        mid = (low + high) // 2
        if char in ['F', 'L']:
            high = mid
        else:
            low = mid + 1
    return low

seats = []
for row in data:
    seat_r = search(row[:7], 127)
    seat_c = search(row[7:], 7)
    seats.append(seat_r * 8 + seat_c)

print('Part1:', max(seats))

for seat in range(min(seats)+1, max(seats)):
    if seat not in seats:
        print('Part2:', seat)
