while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    else:
        print('Enter a Integer value for your age')
while True:
    print('Select a new password (letteres and numbers only):')
    password = input()
    if password.isalnum():
        break
    else:
        print('password only have letteres and numbers')