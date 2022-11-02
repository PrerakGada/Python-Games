def displayboard():
    print("\n")
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|" + board[7] + "|" + board[8])
    print("\n")


def WinLose(g):

    if board[0] == board[1] == board[2] != " ":
        g = False
        if board[0] == "X":
            print("X wins")
        elif board[0] == "O":
            print("O Wins")

    elif board[3] == board[4] == board[5] != " ":
        g = False
        if board[3] == "X":
            print("X wins")
        elif board[3] == "O":
            print("O Wins")

    elif board[6] == board[7] == board[8] != " ":
        g = False
        if board[6] == "X":
            print("X wins")
        elif board[6] == "O":
            print("O Wins")

    elif board[0] == board[3] == board[6] != " ":
        g = False
        if board[0] == "X":
            print("X wins")
        elif board[0] == "O":
            print("O Wins")

    elif board[1] == board[4] == board[7] != " ":
        g = False
        if board[1] == "X":
            print("X wins")
        elif board[1] == "O":
            print("O Wins")

    elif board[2] == board[5] == board[8] != " ":
        g = False
        if board[2] == "X":
            print("X wins")
        elif board[2] == "O":
            print("O Wins")

    elif board[0] == board[4] == board[8] != " ":
        g = False
        if board[1] == "X":
            print("X wins")
        elif board[1] == "O":
            print("O Wins")

    elif board[2] == board[4] == board[6] != " ":
        g = False
        if board[2] == "X":
            print("X wins")
        elif board[2] == "O":
            print("O Wins")

    else:
        if " " not in board:
            print("The Game is Draw!!")
            g = False
    print("\n")
    return g


def move():
    pos = int(input("Enter the location you want to play: "))
    if board[pos - 1] == " ":
        board[pos - 1] = turn
    else:
        print("This place is already filled")
        move()


def player(t):
    if MoveCount % 2 == 0:
        print("It's X's Turn\n")
        t = "X"
    else:
        print("It's O's Turn\n")
        t = "O"
    return t


# Control Code
print("\n\n1|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9\n")
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
Game = True
MoveCount = 0
turn = "X"
displayboard()

while Game:
    turn = player(turn)
    move()
    MoveCount += 1
    displayboard()
    Game = WinLose(Game)
    if not Game:
        print("Do you want to play again?")
        choice = int(input("Enter '1' to Play again: "))
        if choice == 1:
            Game = True
