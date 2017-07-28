class Model:
    def __init__(self):
        self.player_score = 10

    def get_player_score(self):
        return self.player_score

    def add_score(self):
        self.player_score += 1
        print(self.player_score)
