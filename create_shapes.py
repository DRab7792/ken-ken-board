import random

#Assign 11 numbers randomly across the board
def shapePosition():
    board =[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
##    for y in range(6):
##        for x in range(6):
##            board[y][x] = random.randint((y+x)+1,(y+x)+2)
    return board

#Group like numbers together
def groups (board):
    count = 9
    for y in range(6):
        for x in range(6):
            try:
                if x==0 and y==0:
                    board[y][x]=count
                    count +=1
                elif x==0 and y!=0:
                    direction = random.randint(1,3)
                    if direction==1 and board[y][x]==0:
                        board[y][x] = count
                        board[y+1][x] = count
                        count += 1
                    elif direction==2 and board[y][x]==0:
                        board[y][x] = count
                        board[y-1][x] = count
                        count += 1
                    elif direction==3 and board[y][x]==0:
                        board[y][x] = count
                        count += 1
                elif y==0 and x!=0:
                    direction = random.randint(1,3)
                    if direction==1 and board[y][x]==0:
                        board[y][x] = count
                        board[y][x-1] = count
                        count += 1
                    elif direction==2 and board[y][x]==0:
                        board[y][x] = count
                        board[y][x+1] = count
                        count += 1
                    elif direction==3 and board[y][x]==0:
                        board[y][x] = count
                        count += 1
                else:
                    direction = random.randint(1,10)
                    if direction==1 and board[y][x]==0:
                        board[y][x] = count
                        board[y][x-1] = count
                        count += 1
                    elif direction==2 and board[y][x]==0:
                        board[y][x] = count
                        board[y][x+1] = count
                        count += 1
                    elif direction==3 and board[y][x]==0:
                        board[y][x] = count
                        board[y+1][x] = count
                        count += 1
                    elif direction==4 and board[y][x]==0:
                        board[y][x] = count
                        board[y-1][x] = count
                        count += 1
                    elif direction==5 and board[y][x]==0:
                        board[y][x] = count
                        board[y][x-1] = count
                        board[y+1][x] = count
                        count += 1
                    elif direction==6 and board[y][x]==0:
                        board[y][x] = count
                        board[y][x+1] = count
                        board[y-1][x] = count
                        count += 1
                    elif direction==7 and board[y][x]==0:
                        board[y][x] = count
                        board[y+1][x] = count
                        board[y][x-1] = count
                        count += 1
                    elif direction==8 and board[y][x]==0:
                        board[y][x] = count
                        board[y-1][x] = count
                        board[y][x+1] = count
                        count += 1
                    elif direction>8 and direction<11 and board[y][x]==0:
                        board[y][x]=count
                        board[y+1][x]=count
                        board[y][x+1]=count
                        board[y+1][x+1]=count
                        count += 1
            except IndexError:
                board[y][x]=count
    return board, count

#fill in the blank spots that are next to each other
def fillBlanks(board, count):
    blanks = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
    for y in range(6):
        for x in range(6):
            try:
                if board[y][x]!=board[y+1][x] and board[y][x]!=board[y-1][x] and board[y][x]!=board[y][x+1] and board[y][x]!=board[y][x-1]:
                    blanks[y][x]=count
                    count +=1
            except IndexError or TypeError:
                blanks[y][x]=0
    for y in range(6):
        for x in range(6):
            if blanks[y][x]>0 and blanks[y][x+1]>0:
                board[y][x] = count
                board[y][x+1] = count
                count +=1
            elif blanks[y][x]>0 and blanks[y][x-1]>0:
                board[y][x] = count
                board[y][x-1] = count
                count +=1
            elif blanks[y][x]>0 and blanks[y+1][x]>0:
                board[y][x] = count
                board[y+1][x] = count
                count +=1
            elif blanks[y][x]>0 and blanks[y-1][x]>0:
                board[y][x] = count
                board[y-1][x] = count
                count +=1
##    for i in range(6):
##        print (blanks[i])
    return board

#determine the operators for each shape
def operators(board):
    operationBoard = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
    for y in range(6):
        for x in range(6):
            operationBoard[y][x] = board[y][x] %4
    return operationBoard

#Draw the board
##def drawBoard(board):
##    print (" ", end="")
##    for y in range(6):
##        print ("\n")
##        for x in range(6):
##            if board[y][x]!=board[y+1][x] and :
##                print ("_")
            
board = shapePosition()
board, count = groups(board)
board = fillBlanks(board, count)
#drawBoard(board)
operationBoard = operators(board)
for i in range(6):
    print (board[i])
print ("\n")
for i in range(6):
    print (operationBoard[i])
