import arcade
import random
from constants import *


class room():
    def __init__(self):
        super().__init__()
        self.width = 100
        self.height = 100
        self.walls = []
        self.coins = []
        self.player_start = []
        self.next_level = []

    def choose_size(self):
        width = random.randint(400, 800)
        height = random.randint(400, 700)

        self.width = width
        self.height = height

    def add_border(self):
        w = int(self.width / 50)
        h = int(self.height / 50)
        for x in range(w + 1):
            bottom_left = x
            bottom_bottom = 0
            coordinate_bottom = [bottom_left * 50, bottom_bottom * 50]
            self.walls.append(coordinate_bottom)
            top_left = x
            top_bottom = h
            coordinate_top = [top_left * 50, top_bottom * 50]
            self.walls.append(coordinate_top)
        for y in range(h):
            left_left = 0
            left_bottom = y
            coordinate_left = [left_left * 50, left_bottom * 50]
            self.walls.append(coordinate_left)
            right_left = w
            right_bottom = y
            coordinate_right = [right_left * 50, right_bottom * 50]
            self.walls.append(coordinate_right)

    def create_walls(self):

        coordinate = []
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

    def next_level(self):
        w = int(self.width / 50)
        h = int(self.height / 50)
        left = random.randint(1, w - 1)
        for y in range(2):
            bottom = random.randint(1, h - 1)
            if [left, bottom] in self.walls or [left, bottom] in self.coins or [left, bottom] in self.player_start:
                y = 0
            else:
                y = 4
                coordinate = [left * 50, bottom * 50]
                self.next_level.append(coordinate)
