import os
import tkinter as tk
from tkinter import ttk
from gui.controller import GameController
from game.game import Game

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # Get the directory of the current file, will be used to locate resources like images

main = tk.Tk()
main.title("Simple Chess")
main.label = tk.Label(main, text="Simple Chess UI", font=("Helvetica", 16))
main.label.pack(pady=10)
main.config(bg="#070015")
main.geometry("800x700")
main.update_idletasks()

geometryX = 0
geometryY = 0

main.geometry("+%d+%d"%(geometryX, geometryY))

style = ttk.Style(main)
style.theme_use("clam")

menu = tk.Menu(main)
main.config(menu=menu)
menu_0 = tk.Menu(menu, tearoff=0)
menu_0.add_command(label="New", command=lambda: print("New clicked"))
menu_0.add_command(label="Open", command=lambda: print("Open clicked"))
menu.add_cascade(label="File", menu=menu_0)
menu_1 = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=menu_1)

style.configure("WhiteSquare.TButton", background="#E7E7E7", relief="flat") # Set the background color for white squares to a light gray and remove the border relief
style.configure("BlackSquare.TButton", background="#3D3D3D", relief="flat") # Set the background color for black squares to a dark gray and remove the border relief
style.map("WhiteSquare.TButton", background=[("active", "#8f8f8f")], foreground=[("active", "#000")]) # Set the background color for white squares when active to a medium gray and the text color to black
style.map("BlackSquare.TButton", background=[("active", "#8f8f8f")], foreground=[("active", "#000")]) # Set the background color for black squares when active to a medium gray and the text color to black

container = tk.Frame(main, bg="#070015")
container.pack(fill="both", expand=True)

square_buttons = {}  # Dictionary to hold references to the square buttons
game = Game()  # Initialize the game
game_controller = GameController(game)  # Initialize the game controller with the game

# Fixed square board size
tile = 64
board_size = tile * 8

board_frame = tk.Frame(container, width=board_size, height=board_size, bg="#070015")
board_frame.place(relx=0.5, rely=0.5, anchor="center")
board_frame.grid_propagate(False)  # keep exact width/height

for r in range(8):
    board_frame.grid_rowconfigure(r, minsize=tile, weight=1, uniform="row")
for c in range(8):
    board_frame.grid_columnconfigure(c, minsize=tile, weight=1, uniform="col")

for i in range(8):
    for j in range(8):
        file = "abcdefgh"[j]
        rank = str(8 - i)
        sq_style = "WhiteSquare.TButton" if (i + j) % 2 == 0 else "BlackSquare.TButton"
        b = ttk.Button(board_frame, text="", style=sq_style, command=lambda sq=file+rank: game_controller.on_square_click(sq))
        b.grid(row=i, column=j, sticky="nsew")
        square_buttons[file+rank] = b  # Store the button reference in the dictionary

main.mainloop()