pwlist = [str(x) for x in range(168630, 718098 + 1)]

count = 0
for pw in pwlist:
    i = 0
    valid = True
    has_double = False
    while i < 5:
        if int(pw[i]) > int(pw[i+1]):
            valid = False
            break
        if pw.count(pw[i]) == 2:
            has_double = True
        i += 1
    if valid and has_double:
        count += 1

print(count)  # 1145
