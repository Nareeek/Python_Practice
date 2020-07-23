# number patterns
def pattern1(n):
    x = 0
    for i in range(0, n):
        x += 1
        for j in range(0, i + 1):
            print(x, end=" ")
        print("\r")


# pascal's triangle
def pattern2(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print(function(i, j), " ", end="")
        print()


def function(n, k):
    res = 1
    if k > n - k:
        k = n - k
    for i in range(0, k):
        res = res * (n - i)
        res = res // (i + 1)
    return res


# right alphabetical triangle
def pattern3(n):
    x = 65
    for i in range(0, n):
        ch = chr(x)
        x = x + 1
        for j in range(0, i + 1):
            print(ch, end=" ")
        print("\r")


# diamond shape with characters
def pattern4(n):
    k = 2 * n - 2
    x = 65
    for i in range(0, n):
        ch = chr(x)
        x = x + 1
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print(ch, end=" ")
        print("\r")
    k = n - 2
    x = 65
    for i in range(n, -1, -1):
        ch = chr(x)
        x = x + 1
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print(ch, end=" ")
        print("\r")


print(pattern1(7))
print("-" * 15)
print(pattern2(7))
print("-" * 15)
print(pattern3(15))
print("-" * 15)
print(pattern4(15))
