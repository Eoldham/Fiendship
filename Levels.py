import arcade
from Room import *
from constants import *


class allLevels():
    def __init__(self):
        super().__init__()
        self.rooms = []
        self.num_of_rooms = 20

    def create_rooms(self):
        for looper in range(self.num_of_rooms):
            current_room = room()
            current_room.choose_size()
            current_room.add_border()
            room_width = current_room.width
            room_height = current_room.height
            current_room.create_walls()
            current_room.add_fiend_coin()
            current_room.add_player_start()
            current_room.add_next_level()
            current_room.add_monster()
            self.rooms.append(current_room)
