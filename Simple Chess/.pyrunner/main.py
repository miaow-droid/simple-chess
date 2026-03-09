# This code is generated using PyUIbuilder: https://pyuibuilder.com

import os
import tkinter as tk
from tkinter import ttk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


main = tk.Tk()
main.title("Simple Chess")
main.config(bg="#070015")
main.geometry("800x645")
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

style.configure("button.TButton", background="#2b2b2b", foreground="#000", relief=tk.FLAT)
style.map("button.TButton", background=[("active", "#8f8f8f")], foreground=[("active", "#000")])

button = ttk.Button(master=main, text="", style="button.TButton")
button.place(x=160, y=80, width=40, height=40)

style.configure("button1.TButton", background="#E4E2E2", foreground="#000", relief=tk.FLAT)
style.map("button1.TButton", background=[("active", "#8f8f8f")], foreground=[("active", "#000")])

button1 = ttk.Button(master=main, text="", style="button1.TButton")
button1.place(x=120, y=80, width=40, height=40)

style.configure("button2.TButton", background="#2b2b2b", foreground="#000", relief=tk.FLAT)
style.map("button2.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

button2 = ttk.Button(master=main, text="", style="button2.TButton")
button2.place(x=240, y=80, width=40, height=40)

style.configure("button3.TButton", background="#2b2b2b", foreground="#000", relief=tk.FLAT)
style.map("button3.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

button3 = ttk.Button(master=main, text="", style="button3.TButton")
button3.place(x=320, y=80, width=40, height=40)

style.configure("button4.TButton", background="#2b2b2b", foreground="#000", relief=tk.FLAT)
style.map("button4.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

button4 = ttk.Button(master=main, text="", style="button4.TButton")
button4.place(x=400, y=80, width=40, height=40)

style.configure("button5.TButton", background="#E4E2E2", foreground="#000", relief=tk.FLAT)
style.map("button5.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

button5 = ttk.Button(master=main, text="", style="button5.TButton")
button5.place(x=200, y=80, width=40, height=40)

style.configure("button6.TButton", background="#E4E2E2", foreground="#000", relief=tk.FLAT)
style.map("button6.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

button6 = ttk.Button(master=main, text="", style="button6.TButton")
button6.place(x=280, y=80, width=40, height=40)

style.configure("button7.TButton", background="#E4E2E2", foreground="#000", relief=tk.FLAT)
style.map("button7.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

button7 = ttk.Button(master=main, text="", style="button7.TButton")
button7.place(x=360, y=80, width=40, height=40)


main.mainloop()