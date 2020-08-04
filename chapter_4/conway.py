import random, time, sys, copy
WIDTH = 60
HEIGHT = 20

#create a list of list for the cell:
nextCell = []
for x in range (WIDTH):
    column = []                                     #create a new column
    for y in range (HEIGHT):
        if random.randint(0,1) ==0:
            column.append('#')                      #add a living cell
        else:
            column.append(' ')                      #add a dead cell
    nextCell.append(column)                         #nextCell is a list of column list.

#Main program loop
while True:
    print('\n\n\n\n\n')                             #seperate each step with newlines.
    currentCell = copy.deepcopy(nextCell)

    #print currentCell on the Screen
    for y in range (HEIGHT):
        for x in range (WIDTH):
            print(currentCell[x][y],end='')         #print the # or space
        print()                                     #print a new line at the end of the row.

    #calculate the next step's cells based on the current step's cells:
    for x in range (WIDTH):
        for y in range(HEIGHT):
            #get neighboring coordinates:
            # %WIDTH ensures the leftCoord is always between 0 and WIDTH -1
            leftCoord = (x-1) % WIDTH
            rightCoord = (x+1) % WIDTH
            aboveCoord = (y-1) % HEIGHT
            belowCoord = (y+1) % HEIGHT

            #count number of living neighbor:
            numNeighbour = 0
            if currentCell[leftCoord][aboveCoord]== '#':
                numNeighbour +=1    # Top-left neighbor is alive.
            if currentCell[x][aboveCoord] =='#':
                numNeighbour +=1    # Top neighbor is alive.
            if currentCell[rightCoord][aboveCoord] == '#':
                numNeighbour +=1    # Top-right neighbor is alive.
            if currentCell[leftCoord][y] == '#':
                numNeighbour +=1    # Left neighbor is alive.
            if currentCell[rightCoord][y] == '#':
                numNeighbour +=1    # Right neighbor is alive.
            if currentCell[leftCoord][belowCoord] == '#':
                numNeighbour +=1    # Bottom-left neighbor is alive.
            if currentCell[x][belowCoord] == '#':
                numNeighbour +=1    # Bottom neighbor is alive.
            if currentCell[rightCoord][belowCoord] == '#':
                numNeighbour +=1    # Bottom-right neighbor is alive.

            # Set cell based on Conway's Game of Life rules:
            if currentCell[x][y] =='#' and (numNeighbour==2 or numNeighbour==3):
                 # Living cells with 2 or 3 neighbors stay alive:
                nextCell[x][y] = '#'
            elif currentCell[x][y] ==' ' and numNeighbour==3:
                # Dead cells with 3 neighbors become alive:
                nextCell[x][y]=='#'
            else:
                # Everything else dies or stays dead:
                nextCell[x][y]==''
    time.sleep(1)           # Add a 1-second pause to reduce flickering.