import arcade
import random


class generate_room():
    def __init__(self):
        super().__init__()
        self.width = 100
        self.height = 100

    def choose_size(self):
        width = random.randint(200, 800)
        height = random.randint(200, 800)

        self.width = width
        self.height = height

    def create_walls(self):
        wall_list = []
        coordinate = []
        for x in (0,self.width):
            randx = random.randint(0, self.width)
            randy = random.randint(0, self.height)
            if [randx, randy] in wall_list:
                x -= 1
            else:
                coordinate = [randx,randy]
                wall_list.append(coordinate)
                x += 1
