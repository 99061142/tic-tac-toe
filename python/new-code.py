import tkinter as tk

# Makes the window
window = tk.Tk()
window.title('Tic-Tac-Toe')
window.configure(bg="lightgray")

board = [[tk.StringVar(value='X')] * 3] * 3 # Board with the values inside


# If the user press an tile 
def tile_pressed(value):
    # If the tile was empty
    if not value:
        pass


def make_board():
    # For every tile inside the board (3x3)
    for row_index, row in enumerate(board):
        for col_index, value in enumerate(row):
            # Makes the tile
            tile = tk.Button(
                window, 
                borderwidth=2,
                relief="groove",
                text=value.get(),
                width=35,
                height=10,
                command= lambda: tile_pressed(value.get())
            ).grid(row=row_index, column=col_index)




# When the program starts
if __name__ == "__main__":
    board = make_board() # Makes the board
    window.mainloop()