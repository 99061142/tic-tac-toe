import tkinter as tk
from tkinter import ttk

# Makes the window
window = tk.Tk()
window.title('Tic-Tac-Toe')
window.configure(bg="lightgray")

board_list = [[tk.StringVar()] * 3] * 3 # Board with the values inside

player = tk.StringVar() # Player that has the turn


# Show the homescreen
class homescreen:
    def __init__(self, master) -> None:
        self.master = master # Master window
        self.frame = tk.Frame(self.master) # Makes a new frame inside the master window

        # Title
        tk.Label(
            self.frame, 
            text="Tic-Tac-Toe", 
            font=("Arial", 25)
        ).grid(columnspan=3)

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


    def chose_starting_player(self) -> None:
        chosen_player = player.get().upper() # Input of the user

        # If the user chose "x" or "o" as starting player
        if chosen_player == "X" or chosen_player == "O":
            self.frame.destroy() # Destroy the frame of the homescreen
            board(window) # Show the board


# Show the board
class board:
    def __init__(self, master) -> None:
        self.master = master # Master window
        self.frame = tk.Frame(self.master) # Makes a new frame inside the master window

        # Title
        tk.Label(
            self.frame, 
            text="Tic-Tac-Toe", 
            font=("Arial", 25)
        ).grid(columnspan=3)

        self.create_board()

        self.frame.pack() # Add the frame to the window

    def create_board(self) -> None:
        # For every tile inside the board (3x3)
        for row_index, row in enumerate(board_list):
            for col_index, value in enumerate(row):
                # Makes the tile
                tile = tk.Button(
                    self.frame, 
                    borderwidth=2,
                    relief="groove",
                    text=value.get(),
                    width=35,
                    height=10,
                    command= lambda: self.tile_pressed(value.get())
                ).grid(row=row_index+1, column=col_index)

    def tile_pressed(self, value):
        # Tile is empty
        if not value:
            pass


def main():
    # Show the homescreen
    homescreen(window) 
    window.mainloop()




# When the program starts
if __name__ == "__main__":
    main()