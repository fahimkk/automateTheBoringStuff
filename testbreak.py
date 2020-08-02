while True:
    print('Who are you ?')
    name = input()
    if name == 'joe':
        break
print('Hello, Joe. What is the password ?!')
while True:
    password = input()
    if password == 'swordfish':
        break
    else:
        print('Wrong password !, Try agian')
print('Access granted')