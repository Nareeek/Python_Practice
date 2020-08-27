import itertools
x = [1, 2, 3]
a = [p for p in itertools.product(x, repeat=len(x))]

print(a)
