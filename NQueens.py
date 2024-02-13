# This is the NQueens problem. 
# In this problem u have to place N Queens in a nxn Board such that, 
# No Queens are in same rows, columns or Diagonals.

def isSafe(board, row, col):
    # Check for row
    for i in range(len(board)):
        if board[row][i] == True:
            return False
    
    # Check for column
    for i in range(len(board)):
        if board[i][col] == True:
            return False
    
    # Checking for the left Diagonal.
    maxdis = min(row, col)
    for i in range(1, maxdis+1):
        row1 = row - i
        col1 = col - i
        if board[row1][col1] == True:
            return False
    
    # Checking the right Diagonal.
    maxdis = min(row, len(board)- col - 1)
    for i in  range(1, maxdis+1):
        row2 = row - i
        col2 = col + i
        if board[row2][col2] == True:
            return False
    
    return True

def display(board):
    for i in board:
        for j in i:
            if j is True:
                print("Q ", end = "")
            else:
                print("X ", end = "")
        print()

def NQueens(board, row):
    if row == len(board):
        display(board)
        print()
        return 1
    
    count = 0
    for col in range(len(board)):
        if isSafe(board, row, col) is True:
            board[row][col] = True
            count = count + NQueens(board, row + 1)
            board[row][col] = False
      
    return count

n = 4
board = [[False, False, False, False, False], 
         [False, False, False, False, False], 
         [False, False, False, False, False], 
         [False, False, False, False, False],
         [False, False, False, False, False]]

print(NQueens(board, 0))
