import time, sys
indent = 0                   #how many spaces to indent.
indentIncreasing = True      # Whether the indentation increasing or not.

try:
    while True:         #the main programme loop
        print(' '*indent, end='')
        print('**********')
        time.sleep(.1)     #pause for 0.1s

        if indentIncreasing:    #icrease the no of spaces
            indent +=1
            if indent == 5:    # change direction
                indentIncreasing = False

        else:               # Decrease the no of spaces
            indent -=1
            if indent ==0:  # change direction
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()
