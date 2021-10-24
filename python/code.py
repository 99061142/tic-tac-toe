# Makes the tic tac toe board
def make_board():
    board = [] # Board

    # Add the rows to the board
    for i in range(3):
        row = [] # Make a row
        
        # Add 3 columns to the row and add it to the board
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


def player_turn(player: str):    
    player = "X" if player == "O" else "O" # Change the player 

    return player # Return the player that can choose the next position


def winnable_condition(board):
    players = ["X", "O"] # Players

    player_won = False # If the player won the game

    
    # Check if the top to bottom columns are the same player (per row)
    for row in range(3):
        if board[row][0] in players:
            player_won = board[row].count(board[row][0]) == len(board[row])

            if player_won:
                break

    # Check if the left to right columns are the same player (per row)
    if not player_won:
        for col in range(3):
            if board[0][col] in players and board[0][col] == board[1][col] == board[2][col]:
                player_won = True

            if player_won:
                break

    # Check if the top left to bottom right columns are the same player
    if board[0][0] in players and not player_won and board[0][0] == board[1][1] == board[2][2]:
        player_won = True

    # Check if the top right to bottom left columns are the same player
    if board[0][2] in players and not player_won and board[0][2] == board[1][1] == board[2][0]:
        player_won = True


    return player_won # Returns if a user has won the game


def end_text(player: str, player_won, board):
    # Shows the board
    for row in board:
        for col in row:
            print(col, end=" ")
        else:
            print()

    # If a player won
    if player_won:
        player_won_text = "player {} won".format(player)
        
        print(player_won_text)
    
    # If nobody won
    else:
        print("Nobody won")



def show_board(player: str, board):
    player_won = False # Check if the game is over
    turn = 1 # Which turn it is to choose

    # If the game can't be ended
    while not player_won and not turn > 9:
        print(f"Player {player} turn") # Says which player must choose

        # Shows the board 
        for row in board:
            # Show the 3 items of the row
            for position in row:
                print(position, end=" ")

            else:
                print()

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
                    if board[row][col] == "-" and row >= 0 and col >= 0:

                        board[row][col] = player # Change the column to the player 
                        
                        position_gets_chosen = False # Go to the next option for the next user
                    
                    else:
                        print("This position can't be chosen")    

                except (ValueError, IndexError):
                    print("Choose a valid option")

            else:
                turn += 1

                player_won = winnable_condition(board) # Check if the win condition is completed
                
                if not player_won:
                    player = player_turn(player) # Pick the other player
    
    # If someone won, or all the columns are chosen
    else:
        end_text(player, player_won, board)


board = make_board() # Makes the board
starting_player = get_begin_player() # Get the player that wants to start
show_board(starting_player, board) # Shows the board to the user, and let the user pick a position