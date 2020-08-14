import pyinputplus as pyip

while True:
    prompt = 'Do you want to know how to keep an idiot busy for hours? \n'
    response = pyip.inputYesNo(prompt)
    if response == 'no' :
        break

print('Thank You, Have a nice day.')