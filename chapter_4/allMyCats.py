catNames = []
while True:
    print('Enter the name of cat '+ str(len(catNames)+1) +' Or (Enter nothing to stop.)')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]
print('The Cat Names are')
for names in catNames:
    print(names)
print(catNames)