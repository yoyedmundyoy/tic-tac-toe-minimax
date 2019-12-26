board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
players = ['X', 'Y']

def next_move(board, player, box):
    if board[(box-1)//3][(box-1)%3] == ' ':
        board[(box-1)//3][(box-1)%3] = player
    else:
        box = int(input("Invalid choice please pick another box"))
        next_move(board, player, box)

def copy_board(board):
    new_board = []
    for row in board:
        collect = []
        for elem in row:
            collect.append(elem)
        new_board.append(collect)
    return new_board

def check_win(board):
    #Horizontals
    if board[0][0] == board[0][1] == board[0][2]:
        return board[0][0], "Done"
    if board[1][0] == board[1][1] == board[1][2]:
        return board[1][0], "Done"
    if board[2][0] == board[2][1] == board[2][2]:
        return board[2][0], "Done"
    #Verticals
    if board[0][0] == board[1][0] == board[2][0]:
        return board[0][0], "Done"
    if board[0][1] == board[1][1] == board[1][1]:
        return board[0][1], "Done"
    if board[0][2] == board[1][2] == board[2][2]:
        return board[0][2], "Done"
    #Diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0], "Done"
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2], "Done"
    #Check for draw
    draw = True
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                draw = False
    if draw:
        return None, "Draw"
    return None, "Not Done"
