import arcade
from constants import *
from gameview import *

#from tutorial
class WelcomeView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Welcome View", WINDOW_WIDTH/2, WINDOW_HEIGHT/2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Click to advance", WINDOW_WIDTH/2, WINDOW_HEIGHT/2-75,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        instructions_view = GameView()
        self.window.show_view(instructions_view)
