def get_number_of_islands(binaryMatrix):
    bM = binaryMatrix

    island = 0
    rows = len(bM)
    cols = len(bM[0])

    for i in range(rows):
        for j in range(cols):
            if bM[i][j] == 1:
                markIsland(bM, rows, cols, i, j)  # mark -1 and check arround elements
                island += 1

    return island


def markIsland(bM, rows, cols, i, j):
    queue = []
    queue.append([i, j])  # push first element

    while len(queue) != 0:
        item = queue[0]  # pop first element
        del queue[0]

        x = item[0]
        y = item[1]

        if bM[x][y] == 1:
            bM[x][y] = -1  # mark element

            push_If_Valid(queue, rows, cols, x - 1, y)  # left
            push_If_Valid(queue, rows, cols, x, y - 1)  # up
            push_If_Valid(queue, rows, cols, x + 1, y)  # right
            push_If_Valid(queue, rows, cols, x, y + 1)  # down


def push_If_Valid(queue, rows, cols, x, y):
    if (0 <= x < rows) and (0 <= y < cols):
        queue.append([x, y])  # push element


print(get_number_of_islands([[0, 1, 0, 1, 0],
                             [0, 0, 1, 1, 1],
                             [1, 0, 0, 1, 0],
                             [0, 1, 1, 0, 0],
                             [1, 0, 1, 0, 1]]))
