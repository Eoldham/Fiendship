import arcade
from Room import *
from Levels import *
from game3 import *
from constants import *


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

    def up(self):
        pass

    def down(self):
        pass

    def right(self):
        pass

    def left(self):
        pass
