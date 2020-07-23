a = list(range(1000)) * 10 + list(range(1000, 0, -1)) * 10
print(len(a))
sum = 0
d = {}


def krknutyun(masnik: int, a: list):
    s = 0
    for i in range(len(a)):
        s += int(str(masnik) + str(a[i]))
    return s


for i in range(len(a)):
    if a[i] not in d:
        d[a[i]] = krknutyun(a[i], a)
        sum += d[a[i]]
        # print(sum)
    else:
        sum += d[a[i]]
        # print(sum)
        print(time.time())

print(sum)
