n = 1073741823
m = 1071513599
'''
a = []

for i in range(1, len(bin(n)[2:].zfill(8))):
    if bin(n)[2:].zfill(8)[-i] != bin(m)[2:].zfill(8)[-i]:
        print(2**sum(a))
        break
    else:
        a.append(1)
'''
b =  [1 for i in range(1, len(bin(n)[2:].zfill(8))) if bin(n)[2:].zfill(8)[-i] == bin(m)[2:].zfill(8)[-i] else break]

print(len(b))
print(2**len(b))