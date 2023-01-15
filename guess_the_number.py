from random import randint
import tkinter as tk
from tkinter import ttk


class App(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)

        self.commentator = ttk.Label(
            self, text="Guess the number",
            borderwidth=10, relief="groove"
            )
        self.commentator.grid(row=0, column=0, columnspan=6, pady=30)

        self.try1 = ttk.Label(self, borderwidth=4, relief="solid", width=5)
        self.try1.grid(row=3, column=1)
        self.try2 = ttk.Label(self, borderwidth=4, relief="solid", width=5)
        self.try2.grid(row=3, column=2)
        self.try3 = ttk.Label(self, borderwidth=4, relief="solid", width=5)
        self.try3.grid(row=3, column=3)
        self.try4 = ttk.Label(self, borderwidth=4, relief="solid", width=5)
        self.try4.grid(row=3, column=4)
        self.try5 = ttk.Label(self, borderwidth=4, relief="solid", width=5)
        self.try5.grid(row=3, column=5)

        self.entry = ttk.Entry(self)
        self.entry.grid(row=4, column=1, columnspan=3)
        self.submit = ttk.Button(self, text="Submit")
        self.submit.grid(row=4, column=4, columnspan=2)

        self.pack()

    def hit_probability(self) -> str:
        pass


if __name__ == '__main__':
    number: int = randint(0, 100)
    root = tk.Tk()
    root.title("Guess the number")
    root.geometry("200x200")
    app = App(root)
    app.mainloop()
