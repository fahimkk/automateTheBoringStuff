import pyinputplus as pyip

def addsUptoTen(numbers):
    numList = list(numbers)
    for i,num in enumerate(numList):
        numList[i] = int(num)
    if sum(numList) != 10:
        raise Exception ('The digit must add up to 10, not %s.'%(sum(numList)))
    return int(numbers)
response = pyip.inputCustom(addsUptoTen,'Enter:\t')
print('=>',response)