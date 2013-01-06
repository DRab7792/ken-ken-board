#Import the list of possible lines
#Select 6 random lines that all fit with no repeating numbers vertically or horizontally
#Turn those lines into the board

import random

#Check to see if the numbers above repeat
def check(temp, i, board):
    redo = False
    for y in range(i):
        for x in range(6):
            if temp[x]==board[y][x] and redo==False:
                redo = True
    return temp, redo

#Create a list of possible lines on the board based on the file
def createList():
    file = open("possible board.txt", 'r')
    board = []
    possibleLines = []
    for line in file:
        possibleLines.append(line.strip())
    for i in range(6):
        if i!=0:
            redo=True
            while redo==True:
                newLine, redo = check(possibleLines[random.randint(0,719)], i, board)
            board.append(newLine)
        else:
            board.append(possibleLines[random.randint(0,719)])
    return board

#Convert the board to a multidimensional list of integers
def createBoard(oldBoard):
    newBoard =[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
    for y in range(6):
        for x in range(6):
            newBoard[y][x] = int(oldBoard[y][x])     
    return newBoard

#Print the results
def main():
    board = createList()
    board = createBoard(board)
    return board

board = main()
for x in range(6):
    curLine = ""
    for y in range(6):
        curLine += (str(board[x][y])+" ")
    print (curLine)
