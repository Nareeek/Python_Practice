from itertools import product

a = list(product([10, 2], repeat=2))

print(a)

b = []

for i in a:
    b.append("".join(list(map(str, i))))

print(b, type(b))
c = sum(list(map(int, b)))
print(c)
