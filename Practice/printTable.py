tableData = [   ['apples', 'oranges', 'cherries', 'banana', 'mango'],
                ['Alice', 'Bob', 'Carol', 'Daviddd', 'Tom'],
                ['dogs', 'cats', 'moose', 'goose', 'fish'],
                ['aaaaaa', 'bbbbb', 'cccc', 'ddd', 'ee'],
                ['1', '22', '333', '4444', '55555']]

colWidths = []

for line in tableData:
    colWidths.append(len(max(line, key=len)))

print(colWidths)


for j in range(len(tableData[0])):
    for i in range(len(tableData)):
        print(tableData[i][j].rjust(colWidths[i]), end=' ')
    print()


