"""
Starting File that sets up the welcome window and runs the game
"""


import arcade
from gameview import *
from constants import *
from welcomeview import *

def main():
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)
    welcome_view = WelcomeView()
    window.show_view(welcome_view)
    arcade.run()


if __name__ == "__main__":
    main()
