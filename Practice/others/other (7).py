c = [[0, 2], [1], [], [3], [2]]

r = [2]

i = j = q = k = 0
while i < len(r) and j < len(c):
    if r[i] in c[j]:
        if k == 1:
            c[j].remove(r[i])
        k = 1
        j += 1
    else:
        if j == len(c) - 1:
            i += 1
            j = -1
            k = 0
        j += 1 
print(c)