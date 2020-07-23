def get_number_of_islands(binaryMatrix):
    bM = binaryMatrix
    q = 0

    if len(bM) == len(bM[0]) == 1:
        return bM[0][0]

    a = [0 for i in range(len(bM[0]) + 2)]

    bM = [[0] + bM[i] + [0] for i in range(len(bM))]
    bM = [a] + bM + [a]

    for i in range(1, len(bM) - 1):
        for j in range(1, len(bM[i]) - 1):
            if bM[i][j] == 1 and (bM[i][j - 1] + bM[i][j + 1] + bM[i + 1][j]) == 0:
                q += 1

    return q if q else 1
