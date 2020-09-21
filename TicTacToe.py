print("\n\n1|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9\n\n")

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def displayboard():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|"+  board[7] + "|" + board[8])
    print("\n\n")

def move():
    pass

def WinLose():
    if board[0] == board[1] == board[2] != " ":
        if board[0] == "X":
            print("X wins")
        else:
            print("O Wins")

    elif board[3] == board[4] == board[5] != " ":
        if board[0] == "X":
            print("X wins")
        else:
            print("O Wins")

    elif board[6] == board[7] == board[8] != " ":
        if board[0] == "X":
            print("X wins")
        else:
            print("O Wins")

    elif board[0] == board[3] == board[6] != " ":
        if board[0] == "X":
            print("X wins")
        else:
            print("O Wins")

    elif board[1] == board[4] == board[7] != " ":
        if board[0] == "X":
            print("X wins")
        else:
            print("O Wins")

    elif board[2] == board[5] == board[8] != " ":
        if board[0] == "X":
            print("X wins")
        else:
            print("O Wins")
    else:
        move()


# Control Code

displayboard()

MoveCount = 0
for MoveCount in range(9):
    if MoveCount % 2 == 0:
        print("It's X's Turn")
        pos = int(input("Enter the location you want to play: "))
        if board[pos] == " ":
            board[pos-1] = "X"
        else:
            print("This place is already filled")
    else:
        print("It's O's Turn")
        pos = int(input("Enter the location you want to play: "))
        board[pos-1] = "O"
    displayboard()
    WinLose()