import arcade
import random
import math
import sys

from Game2.constants2 import *


class Fiendship(arcade.Window):
    def __init__(self):
        """ Initialize variables """
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)

        self.direction = "right"
        self.set_mouse_visible(False)

        # Room/View variables
        self.room = 0
        self.view_bottom = 0
        self.view_left = 0
        self.walls = [[True for x in range(HEIGHT)] for useless in range(WIDTH)]
        self.doorpos = 0
        self.xpos = 0
        self.ypos = 0

        # Sprite lists
        self.player_list = None
        self.wall_list = None

    def setup(self):
        """ Setup the game (or reset the game) """
        arcade.set_background_color(BACKGROUND_COLOR)

        # sprite setup
        self.wall_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()

        # Room variable setup
        self.view_left = 0
        self.view_bottom = 0
        self.walls = [[True for x in range(HEIGHT)] for x in range(WIDTH)]
        self.xpos = 0
        self.ypos = 0
        self.direction = "right"

        self.create_room()

    def create_room(self):
        self.walls[1][5] = False
        self.xpos = 1
        self.ypos = 5
        self.direction = "right"
        looper = 0

        while looper < 2000:
            looper = looper + 1

            # force finish
            if looper > 1999:
                for x in range(WIDTH - 1):
                    self.walls[x][16] = False
                self.walls[0][16] = True
                self.doorpos = 16
                wall = arcade.Sprite("images/wall.jpg", 1)
                wall.center_x = (WIDTH - 1) * 32
                wall.center_y = 16 * 32
                self.wall_list.append(wall)

            valid = False
            while not valid:
                old_xpos = self.xpos
                old_ypos = self.ypos

                # checks direction then moves a space
                if self.direction == "right":
                    self.xpos = self.xpos + 1
                if self.direction == "left":
                    self.xpos -= 1
                if self.direction == "up":
                    self.ypos += 1
                if self.direction == "down":
                    self.ypos -= 1
                # checks valid movement
                if 0 < self.xpos < WIDTH and 0 < self.ypos < HEIGHT - 1:
                    valid = True

                if not valid:
                    self.xpos = old_xpos
                    self.ypos = old_ypos
                    self.change_direction()

            if valid:
                self.walls[self.xpos][self.ypos] = False
                if random.randint(0, 3) == 2:
                    self.change_direction()

            if self.xpos >= WIDTH - 1:
                self.doorpos = self.ypos
                door = arcade.Sprite("images/castledoors.png")
                door.center_x = self.xpos * 32
                door.center_y = self.ypos * 32
                self.wall_list.append(door)
                break

        end_door = arcade.Sprite("images/castledoors.png")
        end_door.center_x = 0
        end_door.center_y = 5 * 32
        self.wall_list.append(end_door)

    def change_direction(self):
        # randomly change direction
        new_direction = self.direction

        if self.direction == "right" or self.direction == "left":
            if random.randint(0, 1) == 1:
                new_direction = "up"
            else:
                new_direction = "down"
            if self.direction == "up" or self.direction == "down":
                if random.randint(0, 1) == 1:
                    new_direction = "left"
                else:
                    new_direction = "right"

            self.direction = new_direction

    def on_draw(self):
        """ Called when it is time to draw the world """
        arcade.start_render()
        self.wall_list.draw()

    def on_update(self, delta_time):
        """ Called every frame of the game (1/GAME_SPEED times per second)"""


def main():
    window = Fiendship()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
