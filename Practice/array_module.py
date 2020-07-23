import array as arr

a = b = arr.array("i", [1, 2, 3, 5, 6, 4, 6])
print(a)
print(a[2], len(a))

# add element
a.append(467)
print(a)
a.extend([9, 39, 34, 53])
print(a)
a.insert(2, 333333)
print(a)
# a.append(2.4) -> error /dif. type

# remove element
print(b.pop())
print(b.pop(3))
b.remove(4)
print(b)


# concatenation and slicing
print(a)
a = a + a
print(a)
print(a[0:6])
print(a[::-1])

# from array import *

# a = array("i", [1, 2, 3, 5, 6, 4, 6])
# print(a)
