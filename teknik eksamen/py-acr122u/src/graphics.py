from tkinter import *



class Graphics:

    def __init__(self):
        self.window = Tk()

        self.window.geometry("800x400")

        self.text1 = Label(self.window, text="Hello World!", font=("Arial", 25))
        self.text1.pack()

        self.game_mode = Label(self.window, text="none", font=('Arial', 25))
        self.game_mode.pack()

        self.symbol1 = Label(self.window, text="✅", font=(None, 25))
        self.symbol1.pack()

    def update_text(self, text_in):
        """updates the text based on argument, only three elements are expected in text list"""
        temp_text = text_in[0] + text_in[1] + text_in[2]
        self.text1.config(text= text_in) 

    def update_symbol(self, state):
        """takes in the state, and changes the symbol to that state. Only takes in: solved, wrong, none"""
        if state == "solved":
            self.symbol1.config(text="✅")
        if state == "wrong":
            self.symbol1.config(text="❌")
        if state == "none":
            self.symbol1.config(text="")

    def update_game_mode(self, mode):
        """takes in the game_mode that will show on the screen"""
        self.game_mode.config(text=mode)

    def show_error(self):
        ""
