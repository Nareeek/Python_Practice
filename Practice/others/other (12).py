from itertools import permutations

a = [list(permutations(list(range(2000)), 2))]

q = 0

for i in range(len(a)):
    for j in range(len(a[i])):
        q += int(str(a[i][j][0]) + str(a[i][j][1]))
    
    
print(q)