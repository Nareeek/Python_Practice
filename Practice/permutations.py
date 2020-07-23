from itertools import permutations

# 1
a = [list(permutations(list(range(1000, 2000)) + list(range(3000, 1000, -1)), 2))]

q = 0

for i in range(len(a)):
    for j in range(len(a[i])):
        q += int(str(a[i][j][0]) + str(a[i][j][1]))

print(q)

# 2
inp = list(range(6))
q = 0
for z in permutations(inp):
    q += 1
    print(q, end=") (")
