"""
End screen
called when no more rooms
"""
import arcade
from constants import *

class EndView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.PINK_LACE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("You have Completed all levels!", WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Levels change every time you play!", WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 50,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Emily Oldham", WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 100,
                         arcade.color.BLACK, font_size=20, anchor_x="center")

