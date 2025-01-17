"""
Sets up all of the rooms and then makes them into sprites
Each Level is a room class
It works by setting up each rooms coordinates then creating the different
sprites from those coordinates
"""

import arcade
from Room import *
from constants import *


class allLevels():
    def __init__(self):
        super().__init__()
        self.rooms = []
        self.num_of_rooms = 20

    def create_sprite_rooms(self):
        for sprite_room in range(self.num_of_rooms):

            # set up a room that is not a sprite just coordinates
            current_room = room()
            current_room.choose_size()
            current_room.add_border()
            room_width = current_room.width
            room_height = current_room.height
            current_room.create_walls()
            current_room.add_fiend_coin()
            current_room.add_player_start()
            current_room.create_player_boundary()
            current_room.add_next_level()
            current_room.add_monster()

            # set up a sprited room
            room_sprite = roomSprite()

            # add player with coordinates
            start = current_room.player_start
            room_sprite.player_sprite = arcade.Sprite("image/player.png", .25)
            left = start[0]
            bottom = start[1]
            room_sprite.player_sprite.left = left
            room_sprite.player_sprite.bottom = bottom
            room_sprite.player_list.append(room_sprite.player_sprite)

            # add next room portal with coordinates
            end = current_room.next_level
            sprite = arcade.Sprite("image/end.png", .15)
            left = end[0]
            bottom = end[1]
            sprite.left = left
            sprite.bottom = bottom
            room_sprite.next_level.append(sprite)

            # add coins with coordinates
            coins = current_room.coins
            for coin in coins:
                sprite = arcade.Sprite("image/coin.png", .15)
                left = coin[0]
                bottom = coin[1]
                sprite.left = left
                sprite.bottom = bottom
                room_sprite.coin_list.append(sprite)

            # add monster with coordinates
            # chooses which monster is going to be used depending on room number
            monsters = current_room.monsters
            if sprite_room < 5:
                image = "image/monster.png"
            if 5 <= sprite_room < 10:
                image = "image/monster2.png"
            if 10 <= sprite_room < 15:
                image = "image/monster3.png"
            if 15 <= sprite_room <= 20:
                image = "image/monster4.png"
            # Creates the Sprite
            for monster in monsters:
                sprite = arcade.Sprite(image, .25)
                left = monster[0]
                bottom = monster[1]
                sprite.left = left
                sprite.bottom = bottom
                # gives the monster a random speed
                while sprite.change_x == 0 and sprite.change_y == 0:
                    sprite.change_x = random.randrange(-4, 5)
                    sprite.change_y = random.randrange(-4, 5)
                room_sprite.monster_list.append(sprite)

            # add walls with coordinates
            coordinates = current_room.walls
            for coordinate in coordinates:
                wall = arcade.Sprite("image/wall.png", .25)
                left = coordinate[0]
                bottom = coordinate[1]
                wall.left = left
                wall.bottom = bottom
                room_sprite.wall_list.append(wall)

            self.rooms.append(room_sprite)
