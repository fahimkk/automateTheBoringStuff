def spam():
    egg = 'spam local'
    print(egg)  #prints 'spam local'

def balcon ():
    egg = 'balcon local'
    print(egg)  #This will prints 'blacon local'
    spam()
    print(egg)  #prints 'balcon local'

egg = 99

balcon()
print(egg)