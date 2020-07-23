import numpy as np
from matplotlib import pyplot as plt
import seaborn as sb


def s(flip=2):
    x = np.linspace(0, 14, 100)
    for i in range(1, 10):
        plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)
        # yield plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)


sb.set()
s()  # s = s()
plt.show()


# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))


def new(dict):
    for x, y in dict.items():
        yield x, y


a = {1: "HI", 2: "Welcome"}
b = new(a)

print(b)

print(next(b))
print()

print(next(b))
print()
print("-" * 10)


# print(next(b))
# print()


def my_func(i):
    while i <= 3:
        yield i
        i += 1


j = my_func(2)
print(next(j))
print(next(j))
# print(next(j))
print("-" * 10)


def ex():
    n = 3
    yield n
    n = n * n
    yield n


v = ex()
print(next(v))
print(next(v))
# print(next(v))

print("-" * 10)


# for loop
def ex():
    n = 3
    yield n
    n = n * n
    yield n


v = ex()
for x in v:
    print(x)

print("-" * 10)

# iterators and generators
f = range(6)
print("List comp: ", end=":")
q = [x + 2 for x in f]
print(q)

print("gen exp r: ", end=": ")
r = (x + 2 for x in f)
print(r)

print("-" * 10)

print("iterate over generator r-in for loop: ")
for x in r:
    print(x)

print("-" * 10)

# fibonacci numbers
print("fib in generators: ")


def fib():
    f, s = 0, 1
    while True:
        yield f
        f, s = s, f + s


for x in fib():
    if x > 50:
        break
    print(x, end=" ")

print()
print("-" * 10)

# numbers stream
a = range(1, 20, 2)
b = (x for x in a)
print(b)
for y in b:
    print(y)
