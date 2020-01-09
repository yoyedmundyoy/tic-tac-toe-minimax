import math

def print_board(board):
    print("...............")
    print('| ' + board[0][0] + ' || ' + board[0][1] + ' || ' + board[0][2] + ' |')
    print("...............")
    print('| ' + board[1][0] + ' || ' + board[1][1] + ' || ' + board[1][2] + ' |')
    print("...............")
    print('| ' + board[2][0] + ' || ' + board[2][1] + ' || ' + board[2][2] + ' |')
    print("...............")

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
    for player in players:
        if board[0][0] == board[0][1] == board[0][2]==player:
            return board[0][0], "Done"
        if board[1][0] == board[1][1] == board[1][2]==player:
            return board[1][0], "Done"
        if board[2][0] == board[2][1] == board[2][2]==player:
            return board[2][0], "Done"
        #Verticals
        if board[0][0] == board[1][0] == board[2][0]==player:
            return board[0][0], "Done"
        if board[0][1] == board[1][1] == board[1][1]==player:
            return board[0][1], "Done"
        if board[0][2] == board[1][2] == board[2][2]==player:
            return board[0][2], "Done"
        #Diagonals
        if board[0][0] == board[1][1] == board[2][2]==player:
            return board[0][0], "Done"
        if board[0][2] == board[1][1] == board[2][0]==player:
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

def get_best_move(board, player):
    winner_loser = None
    end = None
    winner_loser, end = check_win(board)
    if winner_loser == 'X' and end == "Done":
        return 1
    elif winner_loser == 'O' and end == "Done":
        return -1
    elif end == "Draw":
        return 0

    moves = []
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                empty_cells.append(((i*3)+1)+(j%3))
    
    for cell in empty_cells:
        move = {}
        move['index'] = cell
        new_state = copy_board(board)
        next_move(new_state, player, cell)

        # If AI player
        if player == 'X':
            result = get_best_move(new_state, 'O')
            move['result'] = result
        else:
            result = get_best_move(new_state, 'X')
            move['result'] = result
        
        moves.append(move)
    
    #Find best move
    best_move = None
    if player == 'X':
        best = -math.inf
        for move in moves:
            if move['result'] > best:
                best = move['result']
                best_move = move['index']
    else:
        best = math.inf
        for move in moves:
            if move['result'] < best:
                best = move['result']
                best_move = move['index']
    
    return best_move

if __name__ == "__main__":
    play = 'Y'
    while play == 'Y':
        board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        players = ['X', 'O']
        player = input("Choose which player to start, \'X\' for AI start, \'O\' if you want to start: ")
        if player == 'X' or player =='x':
            player_idx = 0
        elif player == 'Y' or player == 'y':
            player_idx = 1
        current_state = "Not Done"
        winner = None
        print("START!")
        while current_state == "Not Done":
            print_board(board)
            #If AI player
            if player_idx == 0:
                best_box = get_best_move(board, players[player_idx])
                next_move(board, players[player_idx], best_box)
                print("AI plays box: "+str(best_box)+".")
            #If human player
            else: 
                play = int(input("Your turn, enter index of box you wish to play:\t"))
                next_move(board, players[player_idx], play)
            winner, current_state = check_win(board)
            if winner is not None:
                if winner == 'X':
                    print("You have lost to the bot! AI Wins!")
            elif current_state is "Draw":
                print("Draw!")
            player_idx = (player_idx + 1)%2
        play = input("Play again? Y/N:\n")
    print("---Game end gg---")