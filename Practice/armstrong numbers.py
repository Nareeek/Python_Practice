res = []
i = 0
while i < 1e6:
    p = len(str(i))
    s = 0
    for x in str(i):
        s += int(x) ** p
        if s == i:
            res.append(i)
    s = 0
    i += 1

print(res)
