import random

guess = ''
while guess not in ('heads','tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess  = input()

toss = random.randint(0,1) # 0 is tails, 1 is heads
if toss == guess:
    print('YOU got it!')
else: 
    print('Nope! Guess again1')
    guess = input()
    if toss == guess:
        print('You got it This time')
    else:
        print('Nope. You are really bad at this game.')