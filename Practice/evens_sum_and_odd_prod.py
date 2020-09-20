# input bounder A within [0, 10**5]
# input X in range [0, A]
# Sum of all EVEN numbers within range [1, X]
# Product of all ODD numbers within range [1, X]

import sys


A = int(input("Enter a number in range [0, 10**5]: "))

if not(0 <= A <= 1e5):
  raise Exception("Sorry, invalid number")

X = int(input("Enter number in range [0, {}]: ".format(A)))

if not(0 <= X <= A):
  raise Exception("Sorry, invalid number")


summ = 0
prod = 1
i = 0
j = 1

while i < X and j < X:
    summ += i
    # print('i: ', i, ' j: ', j)
    # print('summ:', summ, end = ' ')

    prod *= j
    print('prod:', prod)
    i += 2
    j += 2

print('summ: ', summ)
print('prod: ', prod)
print('-'* 25)
