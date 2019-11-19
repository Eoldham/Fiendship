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
        #flawed math
        wall_list = []
        coordinate = []
        for x in range (int(self.width/50)):
            randx = random.randint(0 + 20, self.width - 20)
            randy = random.randint(0 + 20, self.height - 20)
            if [randx, randy] in wall_list:
                x -= 1
            else:
                coordinate = [randx,randy]
                wall_list.append(coordinate)
                x += 1
        self.coordinates = wall_list
