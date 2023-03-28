def drawLine(x1, x2, y1, y2, board):
    if x1 == y1:
        z = min(x2, y2)
        board[2 * x1 - 1] = board[2 * x1 - 1][:2 * z + 2] + "—" + board[2 * x1 - 1][2 * z + 3:]
    elif x2 == y2:
        z = max(x1, y1)
        board[2 * z - 2] = board[2 * z - 2][:2 * x2 + 1] + "│" + board[2 * z - 2][2 * x2 + 2:]
    else:
        print("Wrong input")


def controlSquare(x1, x2, y1, y2, board, currentPlayer):
    if x1 == y1:
        if "│" in board[2 * x1 - 2][2 * x2 + 1] and "│" in board[2 * x1 - 2][2 * x2 + 3] and "—" in board[2 * x1 - 3]:
            board[2 * x1 - 2] = board[2 * x1 - 2][:2 * x2 + 2] + currentPlayer[0] + board[2 * x1 - 2][2 * x2 + 3:]
        if "│" in board[x1 * 2][2 * x2 + 1] and "│" in board[x1 * 2][2 * x2 + 3] and "—" in board[2 * x1 - 1]:
            board[x1 * 2] = board[x1 * 2][:2 * x2 + 2] + currentPlayer[0] + board[x1 * 2][2 * x2 + 3:]
    elif x2 == y2:  # 1 1 2 1 /2 1 3 1/ 3 2 4 2
        z = max(x1, y1)
        if "—" in board[2 * z - 1][2 * x2 + 2] and "—" in board[2 * z - 3][2 * x2 + 2] and "│" in \
                board[2 * z - 2][2 * x2 + 3]:
            board[2 * z - 2] = board[2 * z - 2][:2 * x2 + 2] + currentPlayer[0] + board[2 * z - 2][2 * x2 + 3:]
        if "—" in board[2 * z - 1][x2 * 2] and "—" in board[2 * z - 3][x2 * 2] and "│" in board[2 * z - 2][2 * x2 + 1]:
            board[2 * z - 2] = board[2 * z - 2][:2 * x2] + currentPlayer[0] + board[2 * z - 2][2 * x2 + 1:]
    else:
        print("Wrong input")


def printBoard(board):
    for k in range(len(board)):
        if k != len(board) - 2:
            print(board[k])


def startGame():
    print("**************************************************\n\nWelcome to DotsAndBoxes "
          "Game\n\n**************************************************\n\nRules:The two players take turns to join two "
          "adjacent dots with a horizontal or vertical line.\nIf a player completes the fourth side of a box they initial "
          "that box and must draw another line.\nWhen all the boxes have been completed the winner is the player who has "
          "initialled the most boxes.")
    player1 = input("First Player's name: ")
    player2 = input("Second Player's name: ")
    row = int(input("Board's row:"))
    column = int(input("Board's column:"))

    maxSquare = (row - 1) * (column - 1) / 2
    currentPlayer = player1
    playerOnePoints = 0
    playerTwoPoints = 0

    a = 0
    m = a

    board = ["———" * column]
    for i in range(row):
        board.append(str(i + 1) + "│ " + "∙ " * column + " │")
        board.append(" │ " + " " * (2 * column) + " │")
    board.append("———" * column)

    printBoard(board)

    while (playerTwoPoints or playerOnePoints) <= maxSquare:
        a = 0
        print(currentPlayer + "'s Turn")
        x1, x2, y1, y2 = list(input("Değeleri giriniz:").split())
        drawLine(int(x1), int(x2), int(y1), int(y2), board)
        controlSquare(int(x1), int(x2), int(y1), int(y2), board, currentPlayer)
        printBoard(board)

        for row in board:
            for index in row:
                if index == currentPlayer[0]:
                    a += 1
        print(currentPlayer + "'s total points:", a)

        if m < a:
            m = a
        else:
            if currentPlayer == player1:
                currentPlayer = player2
            else:
                currentPlayer = player1


startGame()
