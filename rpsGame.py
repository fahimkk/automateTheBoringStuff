import random
import sys
print ('ROCK, PAPER, SCISSORS')
win = 0; losses = 0; ties = 0;
while True: #The main Game loop
    print('%s Wins, %s Losses, %s Ties'%(win,losses,ties))

    while True:     #The player input loop.
        playerMove = input('Enter your move: (r)ock (p)aper (s)cissors or (q)uit \n')
        if playerMove == 'q':
            sys.exit()
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
           break
        print ('Type one of r,p,s or q')

    # Display what the player chose
    if playerMove == 'r':
        print ('ROCK versus...')
    elif playerMove == 'p':
        print ('PAPER versus...')
    elif playerMove == 's':
        print ('SCISSORS versus...')

    # Display what the computer chose
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
        print ('ROCK')
    if randomNumber == 2:
        computerMove = 'p'
        print ('PAPER')
    if randomNumber == 3:
        computerMove = 's'
        print ('SCISSORS')

    # Display and record the win/loss/ties
    if playerMove == computerMove:
        print("It's a Tie")
        ties +=1
    elif playerMove == 'r' and computerMove == 's':
        print ('You Win !')
        win +=1
    elif playerMove == 'p' and computerMove == 'r':
        print ('You Win !')
        win +=1
    elif playerMove == 's' and computerMove == 'p':
        print ('You Win !')
        win +=1
    elif playerMove == 'r' and computerMove == 'p':
        print ('You Lose !')
        losses +=1
    elif playerMove == 'p' and computerMove == 's':
        print ('You Lose !')
        losses +=1
    elif playerMove == 's' and computerMove == 'r':
        print ('You Lose !')
        losses +=1