
def collatz(number):
    if number % 2 ==0:
        return number//2
    else :
        return 3*number+1

def repeat(loop):

    while loop != 1:
        loop = collatz(loop)
        print(loop)
try:
    collatzNumber = int(input('Enter a number: \n'))
    repeat(collatzNumber)
except:
    print('Please enter an integer !!')