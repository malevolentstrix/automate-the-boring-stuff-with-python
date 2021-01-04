# "Debugging Coin Toss" Practice project of Chapter 11
# By JITHIN JOHN
# Code was given in the book itself. The task was just to debug

import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
tossnumber = random.randint(0, 1) # 0 is tails, 1 is heads
toss = ''
if tossnumber == 1:
    toss = 'heads'
else:
    toss = 'tails'
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')