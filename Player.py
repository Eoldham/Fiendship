import arcade
from Room import *
from Levels import *
from game3 import *


class Player:
    def __init__(self):
        super().__init__()
        self.start = []
        self.name = "player"
        self.texture = arcade.load_texture("image/player.png", .25)
        self.left = 0
        self.bottom = 0

    def set_start(self):
        pass

    def set_end(self):
        pass

