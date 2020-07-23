n = 2
k = 3
dp = []
ans = 0

for i in range(n + 1):
    line = []
    for j in range(k + 1):
        line.append(0)
    dp.append(line)

print(dp)