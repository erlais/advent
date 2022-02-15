card_pub = 8184785
door_pub = 5293040

def transform(subject, loop_size, target=None):
    i = 0
    val = 1
    for _ in range(loop_size):
        val *= subject
        val %= 20201227
        i += 1
        if target and val == target:
            return i
    return val

loops_card = transform(7, 100000000, card_pub)
loops_door = transform(7, 100000000, door_pub)
key1 = transform(door_pub, loops_card)
key2 = transform(card_pub, loops_door)
assert key1 == key2
print('Part1:', key1)
