#Creates the game board
board = ["_","_","_",
        "_","_","_",
        "_","_","_",
]

#Conties the game while true
game_is_active = True


winner = None

#Players turn
current_player = "X"


#Handles the functions of the game
def play_game():

    #Displays the intial board
    display_board()

    # continues the game if possible
    while game_is_active:

        #handles a turn while game is still going
        handle_turn(current_player)

        #check if game has ended
        check_game_status()

        #Switch to other player
        change_player()
    
    #Game has ended
    if winner == "X" or winner == "O":
        print(f"{winner} won the game!")
    elif winner == None:
        print("The game was a tie!")


#Displayes the game board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


#allows player to select position in game
def handle_turn(player):

    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")

    valid = False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("Choose a position from 1-9: ")

        position = int(position) - 1

    
        if board[position] == "_":
            valid = True
        else:
            print("Invalid selection. Please go again.")
            

    board[position] = player

    #Updates the board
    display_board()

#Verifies if game is over or can continue
def check_game_status():
    check_winner()
    check_tie()

#checks for rows, columns and diagonals
def check_winner():
    global winner

    row_winner = check_row_win()
    column_winner = check_column_win()
    diagonal_winner = check_diagonal_win()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

    return


def check_row_win():
    global game_is_active
    row_1 = board[0] == board[1] == board[2] != "_"
    row_2 = board[3] == board[4] == board[5] != "_"
    row_3 = board[6] == board[7] == board[8] != "_"

    if row_1 or row_2 or row_3:
        game_is_active = False
    if row_1:
        return board[0]
    elif row_2:
        return board[1]
    elif row_3:
        return board[2]
    return
    
    
def check_column_win():
    global game_is_active
    col_1 = board[0] == board[3] == board[6] != "_"
    col_2 = board[1] == board[4] == board[7] != "_"
    col_3 = board[3] == board[5] == board[8] != "_"

    if col_1 or col_2 or col_3:
        game_is_active = False
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    return

def check_diagonal_win():
    global game_is_active
    diag_1 = board[0] == board[4] == board[8] != "_"
    diag_2 = board[6] == board[4] == board[2] != "_"


    if diag_1 or diag_2:
         game_is_active = False
    if diag_1:
        return board[0]
    elif diag_2:
        return board[6]
    return

def check_tie():
    global board
    global game_is_active
    if "_" not in board:
        game_is_active = False
        return
    return

def change_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return

def game_is_active():
    return

#Begins the game
play_game()
