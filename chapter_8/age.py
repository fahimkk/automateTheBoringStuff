while True:
    print('Enter your Age: ')
    age = input()
    try:
        age = int(age)
    except:
        print('Please use numerical digits')
        continue
    if age<1:
        print('Please enter a positive number')
        continue
    break
print(f'your age is {age}.')