import traceback

def spam():
    bacon()

def bacon():
    raise Exception ('This is the error message.')
try:
    spam()
except :
    errFile = open('errorInfo.txt','w')
    errFile.write(traceback.format_exc())
    errFile.close
    print('The traceback info was written to errorInfo.txt')

print('fahim')