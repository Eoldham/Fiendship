"""
Death screen
called when player health is <= 0
"""

import arcade
from constants import *


class DeadView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.PINK_LACE)


    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("You have Died", WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")

