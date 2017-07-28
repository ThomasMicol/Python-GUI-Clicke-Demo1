from View import *
from Model import *


class Controller:

    def __init__(self):
        self.the_view = View(self)
        self.the_model = Model()
        self.string = "Hello Word"

    def to_string(self):
        return self.string

    def money_click(self):
        self.the_model.add_score()
        self.the_view.update(self.the_model.get_player_score())

    def go(self):
        self.the_view.start()
