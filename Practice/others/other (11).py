import itertools as it
a = list(range(10000))
l = len(a)
k = []
q = 0
for j in it.product(a, repeat = 2):
    k.append(j)
    print(j)

print(k)

for i in range(len(k)):
    q += int(str(k[i][0]) + str(k[i][1]))
    
    
print(q)