import numpy as np
import time
import sys

S = range(1000)
print("size of List range(1000): ", sys.getsizeof(5) * len(S), " bytes")

D = np.arange(1000)
print("size of numpy array range(1000): ", D.size * D.itemsize, " bytes")

print()

size = 100000
l1 = range(size)
l2 = range(size)

a1 = np.arange(size)
a2 = np.arange(size)

print("List time: ")

start = time.time()
result = [(x, y) for x, y in zip(l1, l2)]
print((time.time() - start) * 1000, " (ms * 10^3)")

print("Numpy time: ")

start = time.time()
result = a1 + a2
print((time.time() - start) * 1000, " (ms * 10^3)")
