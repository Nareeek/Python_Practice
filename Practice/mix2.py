import itertools as it

print(it.Predicate(__doc__))

white = []
black = []
letters = "ABCDEFGH"
digits = "12345678"

i = 0
j = 0

while j < 8:
    while i < 8:
        black.append(letters[i] + digits[j])
        i += 1
        j += 1
        black.append(letters[i] + digits[j])
        i += 1
        j -= 1
    j += 2
    i = 0

print(black)

for v, u, w in (1, 2, 3), (4, 5, 6):
    print(v)
    print(u)
    print(w)
