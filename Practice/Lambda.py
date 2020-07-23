from functools import reduce

# lambda arguments:expression

x = lambda a: a * a
print(x(3))  # 9

print("*" * 15)


# def new(a):
#     return a * a
# print(new(3)) # 9

def new_func(x):
    return (lambda y: x + y)


t = new_func(3)
u = new_func(2)

print(t(3))
print(u(3))

print("*" * 15)

my_list = [1, 2, 3, 4, 5, 6]

print("filter: ")
# SYNTAX: filter(function, iterables) return filtered elements
new_list = list(filter(lambda a: (a / 3 == 2), my_list))

print(new_list)

print("*" * 15)

my_list = [1, 2, 3, 4, 5, 6]

print("map: ")
# SYNTAX: map(function, iterables) return the new elements
new_list = list(map(lambda a: (a / 3 != 2), my_list))

print(new_list)

print("*" * 15)

print("reduce: ")
# SYNTAX: reduce(function, sequence)
c = reduce(lambda a, b: a + b, [1, 2, 3, 4, 5, 6j])  # ( ( (23 + 56) + 43) + 98) + 2j
print("sum: ", c)

my_list = [1, 2, 3, 4, 5, 6]

prod = reduce(lambda x, y: x * y, my_list)
# 1 1 = 1
# 2 1 = 2
# ...
# 6 120 = 720
print("prod: ", prod)

greatest = reduce(lambda x, y: y if (y > x) else x, my_list)
# 1 1 = 1
# 2 1 = 2
# ...
# 6 5 = 6
print("max: ", greatest)

print("*" * 15)

# lambda in algebra
print("in algebra: ")
d = lambda x, y: 3 * x + 4 * y
print("3x + 4y: ", d(4, 7))

e = lambda x, y: (x + y) ** 2
print("(x + y)^2 : ", e(4, 7))
