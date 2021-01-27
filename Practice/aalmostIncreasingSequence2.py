def almostIncreasingSequence(s):
    l = []
    for i, j, k in zip(s, s[1:], s[2:] + [10**6]):
        l.append((i >= j) + (i >= k))
        print(l[-1])
        
    print(sum(l))
    return sum(l) < 2


a = [3, 6, 5, 8, 10, 20, 15]


print(almostIncreasingSequence(a))
