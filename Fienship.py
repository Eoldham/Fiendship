import arcade
from gameview import *

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 800
BACKGROUND_COLOR = arcade.color.BLACK
GAME_TITLE = "Fiendship"


def main():
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)
    game_view = GameView()
    window.show_view(game_view)
    arcade.run()


if __name__ == "__main__":
    main()
