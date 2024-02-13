def printboard(board):
    for i in board:
        for j in i:
            print(j + "|", end = " ")
        print()


def Havewon(board, player):
    # check for rows
    for i in range(0, len(board)):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
    # Check for columns
    for j in range(len(board)):
        if board[0][j] == player and board[1][j] == player and board[2][j] == player:
            return True
    # Check for diagonals
    flag = 1
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != player:
                flag = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[len(board) - 1 - i][len(board) - 1 - j] != player:
                flag = 0
    if flag == 1:
        return True
    
    return False

    

    

board = [["", "", ""], ["", "", ""], ["", "", ""]]

player = "X"
GameOver = False
while GameOver!= True:
    printboard(board)
    print("Player " + player + ":" )
    posx = int(input("Please Enter the x poistion: "))
    posy = int(input("Please Enter the y poistion: "))
    if board[posx][posy] == "":
        # Place the X there
        board[posx][posy] = player
        GameOver = Havewon(board, player)
        if GameOver == True:
            print("Player " + player + "have won !")
        else:
            if player == "X":
                player = "O"
            else:
                player = "X"
    else:
        print("Invalid move try again.")

printboard(board)
    