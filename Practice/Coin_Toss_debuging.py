'''Debugging Coin Toss
The following program is meant to be a simple coin toss guessing game. The
player gets two guesses (it’s an easy game). However, the program has several
bugs in it. Run through the program a few times to find the bugs that
keep the program from working correctly.
'''

import random


guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

toss = random.randint(0, 1)  # 0 is tails, 1 is heads

toss = 'heads' if toss else 'tails'

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guesss = input()

    if toss == 'tails':
        tu = "heads"
    else:
        tu = 'tails'

    if toss == guesss:
        print('You got it!')
    elif guesss == tu:
        print("you already answer:{0}\nchange to {1}".format(guesss, toss))
        if input("\ncome on: ") == toss:
            print("finally you win")
        else:
            print('Nope. You are really bad at this game.')
    else:
        print('Nope. You are really bad at this game.')
