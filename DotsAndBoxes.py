a = int(input("sayı:"))
b = int(input("sayı:"))


def drawLine(x1,x2,y1,y2, board):  # 1,1 2,1 / 1,1 1,2
    if x1 == y1:
        board[x1+(x1-1)] = board[x1+(x1-1)][:x2+(x2-1) + 3] + "—" + board[x1+(x1-1)][x2+(x2-1) + 4:]

    elif x2 == y2:
        board[y1+(y1-2)] = board[y1+(y1-2)][:x2+(x2-2) + 3] + "│" + board[y1+(y1-2)][x2+(x2-2) + 4:]

    else:
        print("Wrong input")

def controlSquare():
    print("Square")



def printBoard():
    for k in range(len(board)):
        if k != len(board) - 2:
            print(board[k])


board = ["---" * a]
for i in range(b):
    board.append(str(i + 1) + "| " + "∙ " * a + " |")
    board.append("   " + " " * (2 * a) + "  ")
board.append("---" * a)

drawLine(1,1,1,2,board)
drawLine(1,1,2,1,board)
drawLine(2,1,2,2,board)
drawLine(2,1,3,1,board)
drawLine(4,4,4,5,board)
drawLine(3,3,3,4,board)
drawLine(3,4,4,4,board)
drawLine(3,5,4,5,board)
drawLine(3,4,3,5,board)
drawLine(2,5,2,6,board)
printBoard()

print(len(board[0]))
