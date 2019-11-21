import arcade
from Room import *

class allLevels():
    def __init__(self):
        super().__init__()
        self.rooms = []
        self.num_of_rooms = 20

    def create_rooms(self):
        for looper in range(self.num_of_rooms):
            current_room = room()
            current_room.choose_size()
            current_room.create_walls()
            room_width = current_room.width
            room_height = current_room.height
            current_room.add_border()
            current_room.add_fiend_coin()
            current_room.add_player_start()
            self.rooms.append(current_room)

