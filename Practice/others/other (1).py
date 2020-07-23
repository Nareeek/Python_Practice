def nar(n):
    a = b = n
    t = 1
    while 1:
        if b > 1 and all(b % i for i in range(2, int(b ** .5 + 1))):
            return b
        a -= t
        a, b = b, a
        t *= -1


print(nar(120))