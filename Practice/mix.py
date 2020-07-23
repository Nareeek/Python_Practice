matrix = [[True, False, False, True],
          [False, False, True, False],
          [True, True, False, True]]

for i in range(len(matrix)):
    matrix[i].insert(0, 0)
    matrix[i].append(0)

a = [0 for i in range(len(matrix[0]))]
B = [False for i in range(len(matrix[0]))]
b = [list(B) for i in range(len(matrix) + 2)]

matrix.insert(0, a)
matrix.append(a)

for x in range(1, len(matrix) - 1):
    for y in range(1, len(matrix[0]) - 1):
        b[x][y] = matrix[x - 1][y - 1] + matrix[x - 1][y] + matrix[x - 1][y + 1] + matrix[x][y - 1] + matrix[x][y + 1] + \
                  matrix[x + 1][y - 1] + matrix[x + 1][y] + matrix[x + 1][y + 1]

del b[0]
del b[-1]
for i in b:
    del i[0]
    del i[-1]

print(*b, sep="\n")
