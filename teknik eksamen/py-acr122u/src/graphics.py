from tkinter import *



class Graphics:

    def __init__(self):
        self.window = Tk()

        self.window.geometry("400x400")

        self.text1 = Label(self.window, text="Hello World!", font=("Arial", 25))
        self.text1.pack()

        self.symbol1 = Label(self.window, text="✅", font=(None, 25))
        self.symbol1.pack()

    def update_text(self, text_in):
        """updates the text based on argument"""
        self.text1.config(text= text_in) 

    def update_symbol(self, state):
        """takes in the state, and changes the symbol to that state. Only takes in: solved, wrong, none"""
        if state == "solved":
            self.symbol1.config(text="✅")
        if state == "wrong":
            self.symbol1.config(text="❌")
        if state == "none":
            self.symbol1.config(text="")

    def show_error(self):
        ""

graphics = Graphics()


while True:
    graphics.window.update_idletasks()
    graphics.window.update()
    graphics.update_text(input())
    graphics.update_symbol(input())
