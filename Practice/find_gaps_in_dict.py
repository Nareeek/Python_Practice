numerate1 = {'022': 22,
     '023': 23,
     '024': 24,
     '035': 35,
     '046': 46,
     '057': 57,
     '068': 68,
     '079': 79,
     '080': 80,
     '091': 91}


numerate2 = set()
prev = 0
for val in numerate1.values():
    if val - prev > 1:
        numerate2.add((prev + 1, val - 1))
    prev = val

numerate2 = sorted(list(numerate2))

print(numerate2)
