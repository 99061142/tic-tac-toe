# Makes the tic tac toe board
def make_board():
    board = [] # Board

    # Add the rows to the board
    for i in range(3):
        row = []
        for i in range(3):
            row.append("-")
        else:
            board.append(row)
    else:   
        return board # Returns the board with the rows


# Let the user choose who begins the game
def get_begin_player():
    choosing_starter_player = True # If the player did choose a valid option

    while choosing_starter_player:
        starting_player = input("Do you want to begin with 'X' or with 'O'?: ").upper()

        # Check if the user has chosen between the 2 options
        if starting_player == "X" or starting_player == "O":
            choosing_starter_player = False # Go out of the question

        else:
            print("You can only choose between 'X' or 'O'")

    else:
        return starting_player # Returns the player that starts the game


def player_turn(player):    
    player = 'X' if player == 'O' else 'O' # Change the player 

    return player # Return the player that can choose the next position


def show_board(player):
    game_ended = False # Check if the game is over

    # If the game can't be ended
    while not game_ended:

        print(f"Player {player} turn") # Says which player must choose

        # Shows the board 
        for row in board:
            # Show the 3 items of the row
            for position in row:
                print(position, end=" ")

            else:
                print() # Go to the next row if the 3 items are shown
        else:
            position_gets_chosen = True # If the position must be chosen

            while position_gets_chosen:
                try:
                    # Makes a array out of the chosen numbers 
                    row, col = list(
                        map(int, input("Choose the row and row number to place your stone (example: 1 2): ").split())
                    )

                    # Decrease the numbers (more readable for the user)
                    row -= 1 
                    col -= 1

                    # Check if the position is not already chosen
                    if board[row][col] == "-":

                        board[row][col] = player
                        
                        position_gets_chosen = False # Go to the next option for the next user
                    
                    else:
                        print("This position can't be chosen")    

                except (ValueError, IndexError):
                    print("Choose a valid option")


            else:
                player = player_turn(player) # Pick the other player





board = make_board() # Makes the board
starting_player = get_begin_player() # Get the player that wants to start
show_board(starting_player) # Shows the board to the user, and let the user pick a position