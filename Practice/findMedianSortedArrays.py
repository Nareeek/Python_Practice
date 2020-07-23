def findMedianSortedArrays(nums1, nums2):
    def one(y):
        if len(y) == 1:
            return [y[0]]
        else:
            return y

    def mid(x):
        if len(x) == 0:
            return 0

        if len(x) % 2 == 1:
            return x[len(x) // 2]
        else:
            return (x[len(x) // 2 - 1] + x[len(x) // 2]) / 2
    
    a, b = one(nums1), one(nums2) 
    
    a, b = mid(a), mid(b)
    
    if a:
        if b:
            return (a + b) / 2
        else:
            return a
    elif b:
        return b
    
    else:
        return 0
        


print(findMedianSortedArrays([3], [-2, -1]))


