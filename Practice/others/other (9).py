'''
For a = [10, 2], the output should be concatenationsSum(a) = 1344.

a[0] ∘ a[0] = 10 ∘ 10 = 1010,
a[0] ∘ a[1] = 10 ∘ 2 = 102,
a[1] ∘ a[0] = 2 ∘ 10 = 210,
a[1] ∘ a[1] = 2 ∘ 2 = 22.

'''
k = []
s = 0

a = [1000000, 1000000, 1000000, 1000000]

for i in range(len(a)):
    for j in range(len(a)):
        k.append(str(a[i]) + str(a[j]))
        s += int(k[-1])

print(k)
print(s)


