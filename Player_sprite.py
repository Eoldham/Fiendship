import arcade
from constants import *


class Player(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("images/Player_ex.png", scale=CHARACTER_SCALING)

    def jump(self):
        self.change_y = PLAYER_JUMP_SPEED

    def left(self):
        self.change_x = -PLAYER_MOVEMENT_SPEED

    def right(self):
        self.change_x = PLAYER_MOVEMENT_SPEED

    def release(self):
        self.change_x = 0
