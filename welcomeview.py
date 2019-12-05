import arcade
from constants import *
from gameview import *


class WelcomeView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.BROWN_NOSE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Welcome View", WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 100,
                         arcade.color.PINK_LACE, font_size=50, anchor_x="center")
        arcade.draw_text("Press a key to begin", WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 50,
                         arcade.color.PINK_LACE, font_size=30, anchor_x="center")
        arcade.draw_text("How to play:", WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2,
                         arcade.color.PINK_LACE, font_size=20, anchor_x="center")
        arcade.draw_text("Use the up,left,right and down arrows or wasd to move and use P to sell flowers", WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2-30,
                         arcade.color.PINK_LACE, font_size=20, anchor_x="center")
        arcade.draw_text("Collect flowers by walking over them and attack vegetables by bumping into them", WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 60,
                         arcade.color.PINK_LACE, font_size=20, anchor_x="center")
        arcade.draw_text("Follow all written direction for attacks", WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2-90,
                         arcade.color.PINK_LACE, font_size=20, anchor_x="center")
        arcade.draw_text("There are 20 levels, go to the hole in the dirt to move to the next room",WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2-120,
                         arcade.color.PINK_LACE, font_size=20, anchor_x="center")
        arcade.draw_text("Have Fun! ",WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2-150,
                         arcade.color.PINK_LACE, font_size=20, anchor_x="center")

    def on_key_press(self, symbol: int, modifiers: int):
        game_view = GameView()
        self.window.show_view(game_view)
