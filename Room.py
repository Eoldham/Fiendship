import arcade
import random


class generate_room():
    def __init__(self):
        super().__init__()
        self.width = 100
        self.height = 100
        self.coordinates = []

    def choose_size(self):
        width = random.randint(400, 800)
        height = random.randint(400, 700)

        self.width = width
        self.height = height

    def create_walls(self):
        # flawed math
        wall_list = []
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
                block_number = random.randint(0, int(h / 2) - 1)
                for num in range(block_number):
                    coordinate = [xval*50, yval*50]
                    yval += 1
                    wall_list.append(coordinate)
            else:
                yval = h
                block_number = random.randint(0, int(h / 2) - 1)
                for num in range(block_number):
                    coordinate = [xval*50, yval*50]
                    yval -= 1
                    wall_list.append(coordinate)
        print (wall_list)
        self.coordinates = wall_list
