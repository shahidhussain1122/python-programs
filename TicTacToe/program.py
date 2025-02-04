# complete code for Tic Tac Toe game
# tic tac toe game
player1 = input("Player 1, choose X or O: ")
if player1 == "x":
    player2 = "O"
    player1 = "X"
else:
    player2 = "X"
    player1 = "O"

print(f"Player 1 is {player1} and Player 2 is {player2}")

# board array
board = [" " for x in range(9)]

def startGame():
    print("Welcome to Tic Tac Toe!")
    printBoard()
    playerTurn("1")

def printBoard():
    print("     |     |     ")
    print("  " + board[0] + "  |  " + board[1] + "  |  " + board[2] + "  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print("  " + board[3] + "  |  " + board[4] + "  |  " + board[5] + "  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print("  " + board[6] + "  |  " + board[7] + "  |  " + board[8] + "  ")
    print("     |     |     ")

def playerTurn(turn):
    print(f"Player {turn}, it's your turn.")
    position = input("Choose a position from 1-9: ")
    # keep asking for input until valid position is chosen
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        position = input("Invalid position. Choose a position from 1-9: ")

    # convert position to int
    position = int(position)
    # determine symbol
    symbol = player1 if turn == "1" else player2
    # if choosen position is empty
    if board[position - 1] == " ":
        board[position - 1] = symbol
        printBoard()
        # check if player has won
        if checkWin():
            return
        
        # change turn
        turn = "2" if turn == "1" else "1"
        playerTurn(turn)
    else:
        print("That position is already taken.")
        playerTurn(turn)

def checkWin():
    # check rows
    for i in range(0, 3):
        if board[i] == board[i + 3] == board[i + 6] != " ":
            if board[i] == player1:
                print("Player 1 wins!")
            elif board[i] == player2:
                print("Player 2 wins!")
            return True
    # check columns
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] != " ":
            if board[i] == player1:
                print("Player 1 wins!")
            elif board[i] == player2:
                print("Player 2 wins!")
            return True
    # check diagonals
    if board[0] == board[4] == board[8] != " ":
        if board[0] == player1:
            print("Player 1 wins!")
        elif board[0] == player2:
            print("Player 2 wins!")
        return True
    if board[2] == board[4] == board[6] != " ":
        if board[2] == player1:
            print("Player 1 wins!")
        elif board[2] == player2:
            print("Player 2 wins!")
        return True
    # check if board is full
    if " " not in board:
        print("It's a tie!")
        return True

# start game
startGame()