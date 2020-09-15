q = 0
number = int(input())

while number > 1:
    if number % 2:
        number = number * 3 + 1
    else:
        number //= 2
    q += 1

print(q, " steps")

