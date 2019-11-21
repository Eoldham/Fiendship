import arcade
import os
from Player import *
from Room import *

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 800
BACKGROUND_COLOR = arcade.color.BLACK
GAME_TITLE = "Fiendship"





def main():
    window = Fiendship()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
