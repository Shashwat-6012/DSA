# This is a NKnights problem.
# In this problem we have to place NKnights in the nxn board.
def isSafe(board, row, col):
    # Checking the left two points of knight:
    if col >= 2 and len(board) - row - 1 >= 1 and row >= 1:
        if board[row + 1][col - 2] == True or board[row - 1][col - 2] == True:
            return False
    # Checks for the right two points of knight
    if len(board) - col - 1>= 2 and len(board) - row - 1 >= 1 and row >= 1:
        if board[row + 1][col + 2] == True or board[row - 1][col + 2] == True:
            return False
    # Checks for the upper two points of knight
    if row >= 2 and len(board) - col - 1 >= 1 and col >= 1:
        if board[row - 2][col + 1] == True or board[row - 2][col - 1] == True:
            return False
    # Checks for the Down two points of knight
    if len(board) - row - 1 >= 2 and len(board) - col - 1 >= 1 and col >= 1:
        if board[row + 2][col - 1] == True or board[row + 2][col + 1] == True:
            return False
    
    return True

def display(board):
    for i in board:
        for j in i:
            if j is True:
                print("K ", end = "")
            else:
                print("O ", end = "")
        print()


def Nknights(board, row, col, knights):
    if knights == 0:
        display(board)
        print()
        return
    if row == len(board) - 1 and col == len(board):
        return
    
    if col == len(board):
        Nknights(board, row + 1, 0, knights)
        return
    
    if isSafe(board, row, col):
        board[row][col] = True
        Nknights(board, row, col + 1, knights - 1)
        board[row][col] = False
    
    Nknights(board, row, col + 1, knights)


n = 4
board = [[False]*n for _ in range(n)]
print(Nknights(board, 0, 0, n))
