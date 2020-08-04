import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'very doubtful'

r = random.randint(1,9)
fortune = getAnswer(r)
print(fortune)
#print(getAnswer(random.randint(1,9)))
# OR we can also use the below method

message = ['It is certain','It is decidedly so','Yes','Reply hazy try again','Ask again later','Concentrate and ask again',
          'My reply is no','Outlook not so good','very doubtful']

print(message[random.randint(0,(len(message)-1))])

