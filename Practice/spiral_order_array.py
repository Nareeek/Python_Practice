def spiral_order(arr, end, begin = 0):
    '''
    print the array in spiral order
    '''
    
    i = 0
    j = -1
    end -= 1
    res = []

    while (end - begin >= 0):
        j += 1
        
        # right
        while (begin <= j <= end):
            res.append(arr[i][j])
            # print(arr[i][j], end=' ')
            j += 1
        j -= 1

        i += 1

        # down
        while (begin <= i <= end):
            res.append(arr[i][j])
            # print(arr[i][j], end=' ')
            i += 1
        i -= 1
            
        j -= 1
        end -= 1

        # left
        while (begin <= j <= end):
            res.append(arr[i][j])
            # print(arr[i][j], end=' ')
            j -= 1
        j += 1

        i -= 1
        begin += 1

        # up
        while (begin <= i <= end):
            res.append(arr[i][j])
            # print(arr[i][j], end=' ')
            i -= 1
        i += 1

        #print('begin', begin)
        #print('end: ', end)
        #print()
        
    return res



arr6 =[[ 1, 2, 3, 4, 5, 6],
       [20,21,22,23,24, 7],
       [19,32,33,34,25, 8],
       [18,31,36,35,26, 9],
       [17,30,29,28,27,10],
       [16,15,14,13,12,11]]


arr7 = [[ 1,  2,  3,  4,  5,  6, 7],
        [24, 25, 26, 27, 28, 29, 8],
        [23, 40, 41, 42, 43, 30, 9],
        [22, 39, 48, 49, 44, 31, 10],
        [21, 38, 47, 46, 45, 32, 11],
        [20, 37, 36, 35, 34, 33, 12],
        [19, 18, 17, 16, 15, 14, 13]]


print(spiral_order(arr6, 6))
print(spiral_order(arr7, 7))
