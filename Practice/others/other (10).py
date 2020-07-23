k = []
K = {}

s = 0
a = [10, 2]

for i in range(len(a)):
    for j in range(len(a)):
        k.append(str(a[i]) + str(a[j]))
        s += int(k[-1])

print(s)







