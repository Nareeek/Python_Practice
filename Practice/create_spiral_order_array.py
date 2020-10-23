import pprint

def spiralNumbers(n):
    m = [[0] * n for i in range(n)]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    x, y, c = 0, -1, 1
    for i in range(n + n - 1):
        for j in range((n + n - i) // 2):
            x += dx[i % 4]
            y += dy[i % 4]
            m[x][y] = c
            c += 1
    return m




n = int(input('Enter a number for order: '))
pprint.pprint(spiralNumbers(n))

a = spiralNumbers(n)

print()

for x in a:
    for y in x:
        print(y, end=' ')
    print()


