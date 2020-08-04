birthdays = {'Alice':'April 1', 'Bob':'March 21', 'Carol':'Dec 4'}
while True:
    name = input('Enter a name: (blank to Quit)\n')
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name]+' is the birthday of '+name)
        print()
    else:
        print('I dont have birthday informaton for '+name)
        bday = input('What is their birthday ?\n')
        birthdays[name] = bday
        print('Birthday database updated')
        print()
print(birthdays)