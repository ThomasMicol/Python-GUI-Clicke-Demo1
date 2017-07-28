import tkinter
from tkinter import *


class View:
    def __init__(self, context):
        self.button = 0
        self.frame = Tk()
        self.score_label = Label(self.frame, text="Money: 0")
        self.context = context

    def start(self):
        self.button = Button(self.frame, text="Click for money", command=self.context.money_click)
        self.button.pack()
        mainloop()

    def update(self, new_score):
        self.score_label['text'] = new_score

    def shout(self, message):
        print(message)

    def end(self):
        print("Goodbye!")
        input("Press any key to exit")
