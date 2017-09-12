import tkinter as tk
from tkinter import ttk, N, E, W, S

class Display:
    def __init__(self):
        self.root = tk.Tk()

        self.root.title("Robot Playground")
        for c in range(8):
            self.root.columnconfigure(c, weight=1)
        for r in range(8):
            self.root.rowconfigure(r, weight=1)
        self.board = {}

        for r in range(8):
            for c in range(8):
                lbl = tk.Button(self.root, text="   ")
                lbl["bg"] = "white"
                lbl["font"] = ("Consolas", 12)
                lbl.grid(row=r, column=c, sticky=(N, E, W, S))
                self.board[r,c] = lbl

    def set_cr_action(self, action):
        self.root.bind("<Return>", action)

    def hide(self, robot):
        self.board[robot.row - 1, robot.column - 1]["bg"] = "white"

    def show(self, robot):
        self.board[robot.row - 1, robot.column - 1]["bg"] = robot.colour

    def run(self):
        self.root.mainloop()
