from functools import reduce
from itertools import accumulate

# map(func, iterables)
print("map: ")


def new1(a):
    return a * a


def new2(a, b):
    return a * b


x = map(new1, [1, 2, 3, 4])
print("without lambda1: ", tuple(x))  # list(x), set(x)

y = map(new2, [1, 2, 3, 4], [5, 6, 7, 8])
print("without lambda2: ", tuple(y))  # list(x), set(x)

lst = [1, 2, 3, 4, 5]
y = list(map(lambda x: x + 3, lst))
print("with lambda: ", y)

print("-" * 15)

# filter(functions, iterables)
print("filter: ")


def new1(i):
    if i >= 3:
        return i


j = filter(new1, (1, 2, 3, 4, 5, 6, 7))
print("without lambda: ", tuple(j))

z = filter(lambda x: (x >= 3), (1, 2, 3, 4, 5, 6, 7))
print("with lambda: ", list(z))

print("-" * 15)

# reduce(functions, iterables)
print("reduce: ")


def a(x, y):
    return x + y


s = reduce(a, [1, 3, 4, 5, 6, 7, 7, 8, 8])
print("without lambda: ", s)

s = reduce(lambda q, p: q + p, [1, 3, 4, 5, 6, 7, 7, 8, 8])
print("with lambda: ", s)

print("-" * 15)

# filter within map
print("filter within map: ")

c = map(lambda x: x + x, filter(lambda x: (x >= 4), [2, 3, 4, 5]))
print(tuple(c))

print("-" * 15)

# map within filter
print("map within filter: ")

d = filter(lambda x: (x >= 6), map(lambda x: x + x, [2, 3, 4, 5, 6]))
print(tuple(d))

print("-" * 15)

# map and filter within reduce
print("map and filter within reduce: ")

r = reduce(lambda x, y: x + y, map(lambda x: x + x, filter(lambda x: (x <= 4), [1, 2, 3, 4, 5, 6, 7])))

red = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5, 6, 7])
accum = accumulate([1, 2, 3, 4, 5, 6, 7], lambda x, y: x + y)

print(r)

print("-" * 15)

print("reduce: ", red)
print("accumulate: ", list(accum))
