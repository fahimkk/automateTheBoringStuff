import random
print("I'm thinking of number between 1 and 5")
myNum = random.randint(1,5)
noOfAttempt = 1
while True:
    guess = int(input('Take a guess: \n'))
    if myNum == guess:
        print('Good job! You guessed my number in ' + str(noOfAttempt) + ' attempts')
        break
    elif myNum > guess:
        print('Your guess is too low')
    else:
        print ('your guess is too high')
    noOfAttempt = noOfAttempt + 1