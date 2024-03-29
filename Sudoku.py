import random

def displayBoard():
    print 
    print("+-------+-------+-------+")
    print("| " + board[0][0] + " " + board[0][1] + " " + board[0][2] + " | " + board[1][0] + " " + board[1][1] + " " + board[1][2] + " | " + board[2][0] + " " + board[2][1] + " " + board[2][2] + " |")
    print("| " + board[0][3] + " " + board[0][4] + " " + board[0][5] + " | " + board[1][3] + " " + board[1][4] + " " + board[1][5] + " | " + board[2][3] + " " + board[2][4] + " " + board[2][5] + " |")
    print("| " + board[0][6] + " " + board[0][7] + " " + board[0][8] + " | " + board[1][6] + " " + board[1][7] + " " + board[1][8] + " | " + board[2][6] + " " + board[2][7] + " " + board[2][8] + " |")
    print("+-------+-------+-------+")
    print("| " + board[3][0] + " " + board[3][1] + " " + board[3][2] + " | " + board[4][0] + " " + board[4][1] + " " + board[4][2] + " | " + board[5][0] + " " + board[5][1] + " " + board[5][2] + " |")
    print("| " + board[3][3] + " " + board[3][4] + " " + board[3][5] + " | " + board[4][3] + " " + board[4][4] + " " + board[4][5] + " | " + board[5][3] + " " + board[5][4] + " " + board[5][5] + " |")
    print("| " + board[3][6] + " " + board[3][7] + " " + board[3][8] + " | " + board[4][6] + " " + board[4][7] + " " + board[4][8] + " | " + board[5][6] + " " + board[5][7] + " " + board[5][8] + " |")
    print("+-------+-------+-------+")
    print("| " + board[6][0] + " " + board[6][1] + " " + board[6][2] + " | " + board[7][0] + " " + board[7][1] + " " + board[7][2] + " | " + board[8][0] + " " + board[8][1] + " " + board[8][2] + " |")
    print("| " + board[6][3] + " " + board[6][4] + " " + board[6][5] + " | " + board[7][3] + " " + board[7][4] + " " + board[7][5] + " | " + board[8][3] + " " + board[8][4] + " " + board[8][5] + " |")
    print("| " + board[6][6] + " " + board[6][7] + " " + board[6][8] + " | " + board[7][6] + " " + board[7][7] + " " + board[7][8] + " | " + board[8][6] + " " + board[8][7] + " " + board[8][8] + " |")
    print("+-------+-------+-------+")
    print()

def check():
    for square in board:
        for x in range(9):
            for y in range(x+1, 9):
                if square[x] == square[y]:
                    return False

    return True

def turn():
    x = int(input('Enter the position of X: '))
    y = int(input('Enter the position of Y: '))

    if 0 > x > 9 or 0 > y > 9:
        return False

    num = input('Enter the Value: ')
    board[x-1][y-1] = str(num)

    return True

def setBoard(b):
    num = 1
    for x in range(9):
        for y in range(9):
            b[x][y] = str(random.randint(1, 9))

    return b


    
# Driver Code

print("+-------+-------+-------+")
print("| 1 2 3 | 1 2 3 | 1 2 3 |")
print("| 4 5 6 | 4 5 6 | 4 5 6 |")
print("| 7 8 9 | 7 8 9 | 7 8 9 |")
print("+-------+-------+-------+")
print("| 1 2 3 | 1 2 3 | 1 2 3 |")
print("| 4 5 6 | 4 5 6 | 4 5 6 |")
print("| 7 8 9 | 7 8 9 | 7 8 9 |")
print("+-------+-------+-------+")
print("| 1 2 3 | 1 2 3 | 1 2 3 |")
print("| 4 5 6 | 4 5 6 | 4 5 6 |")
print("| 7 8 9 | 7 8 9 | 7 8 9 |")
print("+-------+-------+-------+")



board = [
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."]
    ]

displayBoard()

game = False

"""while game:
    game = turn()
    displayBoard()"""

board = setBoard(board)
displayBoard()
game = check()

if game:
    print("Sudoku Solved!")
else:
    print("Wrong Solution!")