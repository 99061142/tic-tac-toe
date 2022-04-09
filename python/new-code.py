import tkinter as tk
from tkinter import ttk

# Makes the window
window = tk.Tk()
window.title('Tic-Tac-Toe')
window.configure(bg="lightgray")

# Title
tk.Label(
    window, 
    text="Tic-Tac-Toe", 
    font=("Arial", 25)
).pack(fill='x')

# Board with the values inside
board_list = [
    [
        tk.StringVar(),
        tk.StringVar(),
        tk.StringVar()
    ],
    [
        tk.StringVar(),
        tk.StringVar(),
        tk.StringVar()
    ],
    [
        tk.StringVar(),
        tk.StringVar(),
        tk.StringVar()
    ]
]

player = tk.StringVar() # Player that has the turn

# Make a 2d list of the board with the values of the stringvars
def get_board_list_values() -> list:
    board_list_values = []

    for row_values in board_list:
        board_list_values.append([value.get() for value in row_values])

    return board_list_values


# Check if the board is full 
def board_full(board_list_values) -> bool:
    for row_values in board_list_values:
        for value in row_values:
            if value:
                return False

    return True


# Show the homescreen
class homescreen:
    def __init__(self):
        self.master = window # Master window
        self.frame = tk.Frame(self.master) # Makes a new frame inside the master window

        # Question
        tk.Label(
            self.frame, 
            text="Starting player (x / o):", 
            font=("Arial", 15)
        ).grid(row=1, column=1)
        
        # Input for the user
        ttk.Entry(
            self.frame,
            textvariable=player
        ).grid(row=1, column=2)

        # Submit button
        tk.Button(
            self.frame, 
            text="Submit", 
            command=self.chose_starting_player
        ).grid(columnspan=3, sticky="WE")

        self.frame.pack() # Add the frame to the window


    def chose_starting_player(self):
        chosen_player = player.get().upper() # Input of the user

        # If the user chose "x" or "o" as starting player
        if chosen_player == "X" or chosen_player == "O":
            player.set(player.get().upper()) # Uppercase the player the user chose

            self.frame.destroy() # Destroy the frame of the homescreen
            game() # Show the board


# Show the board
class game:
    def __init__(self):
        self.master = window # Master window
        self.frame = tk.Frame(self.master) # Makes a new frame inside the master window

        # For every tile inside the board (3x3)
        for row, row_values in enumerate(board_list):
            for col, value in enumerate(row_values):
                # Makes the tile
                tk.Button(
                    self.frame, 
                    borderwidth=2,
                    relief="groove",
                    textvariable=value,
                    width=35,
                    height=10,
                    command=lambda row=row, col=col: self.tile_pressed(row, col)
                ).grid(row=row+1, column=col)

        self.frame.pack() # Add the frame to the window

    def tile_pressed(self, row, col):
        # If the tile is empty
        if not board_list[row][col].get():
            board_list[row][col].set(player.get()) # Set the value to the player that has the turn

            self.switch_player()

    def switch_player(self):
        player.set("X" if player.get() == "O" else "O") # Switch the players turn

        self.check_board() # Check if the game is over

    def check_board(self):
        board_list_values = get_board_list_values() # Get the 2d board with the values inside it

        # Check every horizontal line
        for row_values in board_list_values:
            # If every horizontal value is the same
            if row_values[0] and all(value == row_values[0] for value in row_values):
                self.game_won(row_values[0])

        # Check every vertical line
        for col in range(3):
            # If every vertical value is the same
            if board_list_values[0][col] and board_list_values[0][col] == board_list_values[1][col] == board_list_values[2][col]: 
                self.game_won(board_list_values[0][col])

        # Check left top to bottom right if the value is the same
        if board_list_values[0][0] and board_list_values[0][0] == board_list_values[1][1] == board_list_values[2][2]:
            self.game_won(board_list_values[0][0])

        # Check bottom right to right top if the value is the same
        if board_list_values[0][2] and board_list_values[0][2] == board_list_values[1][1] == board_list_values[0][2]:
            self.game_won(board_list_values[0][2])

        # If the board is full and nobody won
        if board_full(board_list_values):
            self.game_tie()

    def game_won(self, player_won):
        self.frame.destroy() # Delete the board
        endscreen().won(player_won) # Show the player that has won the game

    def game_tie(self):
        self.frame.destroy() # Delete the board
        endscreen().tie() # Show that the game is a tie


class endscreen:
    def __init__(self):
        self.master = window # Master window
        self.frame = tk.Frame(self.master) # Makes a new frame inside the master window
        self.frame.pack() # Add the frame to the window
    
    def won(self, player):
        text = f"Player \"{player}\" has won the game" # Text who won the game
        bg = "green" # Background color

        self.show_game_over(text, bg)

    def tie(self):
        text = "The game is a tie" # Text that the game is a tie
        bg = "red" # Background color

        self.show_game_over(text, bg)

    def show_game_over(self, text, bg):
        # Text that shows if someone won the game, or that the game is a tie
        tk.Label(
            self.frame, 
            text=text, 
            font=("Arial", 25),
            fg=bg
        ).grid()


def main():
    # Show the homescreen
    homescreen() 
    window.mainloop()




# When the program starts
if __name__ == "__main__":
    main()