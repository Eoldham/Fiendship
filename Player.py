import arcade


class Player():
    def __init__(self):
        super().__init__()
        self.start = []
        self.name = "player"
        self.texture = arcade.load_texture("image/player.png", .25)
        self.left = 0
        self.bottom = 0

    def setStart(self):
        self.left = self.start[0]
        self.bottom = self.start[1]
