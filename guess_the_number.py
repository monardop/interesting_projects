from random import randint
import tkinter as tk
from tkinter import ttk


class App(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Guess the number")

        for n in range(5):
            self.columnconfigure(n, weight=1)

        self.commentator = ttk.Label(self, text="Hola buenos dias", borderwidth=2, relief="solid")
        self.commentator.grid(row=1, column=1, columnspan=3, rowspan=2)

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
        self.entry.grid(row=4, column=2)

        self.pack()



def hit_probability() -> str:
    pass


if __name__ == '__main__':
    number: int = randint(0, 100)
    root = tk.Tk()
    app = App(root)
    app.mainloop()
