s = "codesignalIsAwesome" #"codesignal is awesome"
s = list(s)
a = []

for i in range(len(s)):
    if s[i].isupper():
        a.append(i)
        s[i] = s[i].lower()
ss = list(s)
print(a)

i = 0
j = -1 if a[0] == 0 else 0

while i < len(a) and j < len(a):
    if a[i] != 0:
        ss.insert(a[i] + j, ".")
        j += 1
        i += 1
    else:
        j += 1
        i += 1
    
print(ss)
s = "".join(ss)
s = s.split(".")
print(s)
    