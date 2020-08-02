#empy strig and 0 are considered as false.
name = ''
while not name:
    print('Enter your Name:')
    name = input()
print('How many guest will you have?')
noOfGust=int(input())
if noOfGust :
    print('Be sure to have enough room for all your guest')
print('Done')