"""
Room class, this is how each level is procedurally generated.
"""

import arcade
import random
from constants import *


class room:
    def __init__(self):
        super().__init__()
        self.width = 100
        self.height = 100
        self.walls = []
        self.coins = []
        self.player_start = []
        self.next_level = []
        self.monsters = []
        self.player_boundary = []

    # Sets the size of the room
    def choose_size(self):
        width = random.randint(400, 800)
        height = random.randint(400, 700)

        self.width = width
        self.height = height

    """
    This function creates the border
    By dividing by 50 I am able to make a tiled map
    """

    def add_border(self):
        w = int(self.width / 50)
        h = int(self.height / 50)
        # Creates the bottom and top borders
        for x in range(w + 1):
            bottom_left = x
            bottom_bottom = 0
            coordinate_bottom = [bottom_left * 50, bottom_bottom * 50]
            self.walls.append(coordinate_bottom)
            top_left = x
            top_bottom = h
            coordinate_top = [top_left * 50, top_bottom * 50]
            self.walls.append(coordinate_top)
        # creates the left and right borders
        for y in range(h):
            left_left = 0
            left_bottom = y
            coordinate_left = [left_left * 50, left_bottom * 50]
            self.walls.append(coordinate_left)
            right_left = w
            right_bottom = y
            coordinate_right = [right_left * 50, right_bottom * 50]
            self.walls.append(coordinate_right)

    """
    This function creates the walls.
    The walls are created by choosing first if the wall will jut from the top or bottom border
    Then the wall is given a certain number of blocks (no more than half of the height) creating one line of wall
    This loops the same number of times as the width length
    There is also a checker that each coordinate is placed in to make sure there is no overlap
    """
    def create_walls(self):
        checker = []
        w = int(self.width / 50)
        h = int(self.height / 50)

        for x in range(w):
            for looper in range(2):
                xval = random.randint(1, w - 2)
                if xval in checker:
                    looper = 0
                else:
                    looper = 1
                    checker.append(xval)
                if random.randint(0, 2) == 1:
                    yval = 0
                    block_number = random.randint(1, int(h / 2) - 1)
                    for num in range(block_number):
                        coordinate = [xval * 50, yval * 50]
                        yval += 1
                        self.walls.append(coordinate)
                else:
                    yval = h
                    block_number = random.randint(1, int(h / 2) - 1)
                    for num in range(block_number):
                        coordinate = [xval * 50, yval * 50]
                        yval -= 1
                        self.walls.append(coordinate)

    """
    This function adds the flowers.
    It works by choosing a number in the range (1,4) then creating that number of coins
    the coins are created using the same idea as the walls but now the coin coordinates are checked against the walls
    """
    def add_fiend_coin(self):
        w = int(self.width / 50)
        h = int(self.height / 50)
        coin_num = random.randint(1, 4)
        for c in range(coin_num):
            left = random.randint(1, w - 1)
            for y in range(2):
                bottom = random.randint(1, h - 1)
                coordinate = [left * 50, bottom * 50]
                if coordinate in self.walls:
                    left = random.randint(1, w - 1)
                    y = 0
                else:
                    coordinate = [left * 50, bottom * 50]
                    self.coins.append(coordinate)
                    break

    """
    This function creates a start coordinate for the player. 
    It is very similar to the coins but it just creates one coordinate and is compared to the coin and wall list
    """
    def add_player_start(self):
        w = int(self.width / 50)
        h = int(self.height / 50)
        left = random.randint(1, w - 1)
        for t in range(3000):
            bottom = random.randint(1, h - 1)
            coordinate = [left * 50, bottom * 50]
            if not (coordinate in self.walls or coordinate in self.coins):
                coordinate = [left * 50, bottom * 50]
                self.player_start.append(coordinate[0])
                self.player_start.append(coordinate[1])
                break

    """
    This function adds the hole in the ground.
    It is a singular coordinate like the player start and is checked against the wall, coins and start list
    """
    def add_next_level(self):
        w = int(self.width / 50)
        h = int(self.height / 50)
        left = random.randint(1, w - 1)
        for t in range(10000):
            bottom = random.randint(1, h - 1)
            coordinate = [left * 50, bottom * 50]
            player = [self.player_start[0], self.player_start[1]]
            if not (
                    coordinate in self.walls or coordinate in self.coins or coordinate in player or coordinate in self.monsters or coordinate in self.player_boundary):
                coordinate = [left * 50, bottom * 50]
                self.next_level.append(coordinate[0])
                self.next_level.append(coordinate[1])
                break
    """
    This adds the vegetables.
    This is very similar to the coins, it chooses a certain number of monsters and then sets up the coordinates for them
    """
    def add_monster(self):
        w = int(self.width / 50)
        h = int(self.height / 50)
        monster_num = random.randint(1, 5)
        for m in range(monster_num):
            left = random.randint(1, w - 1)
            for y in range(2):
                bottom = random.randint(1, h - 1)
                coordinate = [left * 50, bottom * 50]
                player = [self.player_start[0], self.player_start[1]]
                end = [self.next_level[0], self.next_level[1]]
                if coordinate in self.walls or coordinate in self.coins or coordinate in player or coordinate in end:
                    left = random.randint(1, w - 1)
                    y = 0
                else:
                    coordinate = [left * 50, bottom * 50]
                    self.monsters.append(coordinate)
                    break

    """
    This is different from the other functions it creates a square around the players start so that the next_level can 
    not be right next to the player when starting. 
    """
    def create_player_boundary(self):
        avoid = []
        beginning_xval = self.player_start[0]
        beginning_yval = self.player_start[1]
        avoid.append(self.player_start)
        for x in range(50):
            xval = beginning_xval + x
            for y in range(50):
                yval = beginning_yval + y
                avoid.append([xval, yval])
        for x in range(50):
            xval = beginning_xval - x
            for y in range(50):
                yval = beginning_yval - y
                avoid.append([xval, yval])
        self.player_boundary = avoid

"""
This class holds all of the lists for the roomSprites that are created in the Level file
"""
class roomSprite:
    def __init__(self):
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.monster_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.next_level = arcade.SpriteList()
        self.player_sprite = arcade.Sprite()
