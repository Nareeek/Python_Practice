def ak(m,n):
    if m == 0:
        return (n + 1)

    if m > 0 and n == 0:
        return ak(m - 1, 1)

    if m > 0 and n > 0:
        return ak(m - 1, ak(m, n - 1))

print(ak(4, 4))
