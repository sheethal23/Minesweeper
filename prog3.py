#!/usr/bin/python3

                   import time        #importing time function from time module
from random import seed, randint               #from random module importing seed,randint functions


'''
Driver routine that calls the solveNQueens for values between 1 and 8
'''
def driver():
    for N in range(1,9):                       #value of N between 1 and 8
        solveNQueens(N)                        #calling of solveNQueens routine


'''
Initializes a RNG with a chosen seed value and creates 2-d list and sets 
every value of matrix to False. Returns board to the following routine 
'''
def initBoard(N):
    seed(time())                               #initializing a RNG with chosen seed value using system time
    board = []                                 #creating 2-d list
    for i in range(N):
        row = []
        for j in range(N):
            row.append(False)
        board.append(row)                      #sets each value of the list to False
    return board                               #returns initial board to the following routine


'''
This routine places the N queens on the board and calls the routine 
solveNQueensUtill. If the return value of solveNQueensUtill is true
then it calls printBoard routine to print out the contents
'''
def solveNQueens(N):
    board = initBoard(N)                       #calling of routine initial board of size N
    print("\nBoard Size = " + str(N))          #printing the size of the board
    if(solveNqueensUtil(board,0)):             #if return value is true then it calls printBoard routine
        printBoard(board)
    else:
        print("solution doest not exists.")


'''
This recursive routine starts on the row number row and gets a random 
column number col, between 0 and len(board)-1 from the RNG, 
and it checks if a queen can be placed on the location (row, col)
'''
def solveNqueensUtil(board,row):
    if row >= len(board):                      #checks if row is greater than board length if true returns true
        return True
    for i in range(len(board)):
        col = randint(0, len(board)-1)         #generates a random col number using randint function
        if(isSafe(board, row, col)):           #checks if quuen can be placed by calling isSafe routine
            board[row][col] = True
            if(solveNqueensUtil(board, row + 1)): #recursive routine to place rest of queens
                return True                        
            board[row][col] = False            #if doesnt leads to a solution 
    return False                               #if queen cannot be placed in any row in this col return false


'''
This routine checks if a queen can be placed in the row number row and
the column number col on the board. If the answer is yes, then it 
returns true.
'''
def isSafe(board, row, col):
    for i in range(len(board)):                #check row on left side
        if board[i][col]:
             return False
    for i in range(len(board)):                #checks for the diagonal
        for j in range(len(board)):
            if board[i][j]:
                x = abs(row - i)
                y = abs(col - j)
                if x==y:
                    return False
    return True


'''
This routine prints the final state of the board as a properly-formatted
rectangular table.
'''
def printBoard(board):
    print('', '-' * ((5 * len(board)) + (len(board) - 1)))
    for i in range(len(board)):
        for k in range(len(board)):           #rows
            print("|", " " * 4, end="")
        print("|")
        for j in range(len(board)):         
            if board[i][j]:                   #checking if queens can be possible in this position of board
                print("|" + "  " + "Q  ", end="")#if yes placing the queens
            else:
                print("|", " " * 4, end="")
        print("|")
        for k in range(len(board)):           #rows
            print("|", ' ' * 4, end='')
        print("|")
        print('', '-' * ((5 * len(board)) + (len(board) - 1)))

                    
driver()              #calling driver function 









