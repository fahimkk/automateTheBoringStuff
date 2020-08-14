import pyinputplus as pyip
import random , time

noOfQuestion = 10
correctAnswer = 0

for questionNo in range (noOfQuestion):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    prompt = '#%s:\t%s x %s =\t'%(questionNo+1,num1,num2)
    try:
        pyip.inputStr(prompt,allowRegexes=['^%s$'%(num1 * num2)],
        blockRegexes=[('.*','Incorrect!')],timeout=8,limit=2)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        print('Correct !')
        correctAnswer+=1
        time.sleep(1)
print('Score: %s/%s'%(correctAnswer,noOfQuestion))