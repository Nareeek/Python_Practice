c = [[0, 2], [1], [], [3], [2], []]
i = 0

while i < len(c):
    if len(c[i]) == 0:
        c.remove(c[i])
        i = 0
    else:
        i += 1
        
print(c)
    
    
    
    
    


