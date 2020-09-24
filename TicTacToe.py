print("\n\n1|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9\n\n")

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def displayboard():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|"+  board[7] + "|" + board[8])
    print("\n")

def WinLose():
    if board[0] == board[1] == board[2] != " ":
        Game = False
        if board[0] == "X":
            print("X wins")
        elif board[0] == "O":
            print("O Wins")
        else:
            Game = True

    elif board[3] == board[4] == board[5] != " ":
        Game = False
        if board[3] == "X":
            print("X wins")
        elif board[3] == "O":
            print("O Wins")
        else:
            Game = True

    elif board[6] == board[7] == board[8] != " ":
        Game = False
        if board[6] == "X":
            print("X wins")
        elif board[6] == "O":
            print("O Wins")
        else:
            Game = True

    elif board[0] == board[3] == board[6] != " ":
        Game = False
        if board[0] == "X":
            print("X wins")
        elif board[0] == "O":
            print("O Wins")
        else:
            Game = True

    elif board[1] == board[4] == board[7] != " ":
        Game = False
        if board[1] == "X":
            print("X wins")
        elif board[1] == "O":
            print("O Wins")
        else:
            Game = True

    elif board[2] == board[5] == board[8] != " ":
        Game = False
        if board[2] == "X":
            print("X wins")
        elif board[2] == "O":
            print("O Wins")
        else:
            Game = True
        
    else:
        if " " not in board:
            print("The Game is Draw!!")
            Game = False


def move():
    displayboard()

    pos = int(input("Enter the location you want to play: "))
    if board[pos] == " ":
        board[pos-1] = turn
        WinLose()
    else:
        print("This place is already filled") 
        move()

        
def player(t):
    if MoveCount % 2 == 0:
        print("It's X's Turn")
        t = "X"
    else:
        print("It's O's Turn")
        t = "O"
    return t

# Control Code
Game = True
MoveCount = 0
turn = "X"

while Game:
    turn = player(turn)
    move()
    MoveCount += 1
    WinLose()
