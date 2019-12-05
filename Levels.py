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

            # set up a room that is not a sprite
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

            # add player
            start = current_room.player_start
            room_sprite.player_sprite = arcade.Sprite("image/player.png", .15)
            left = start[0]
            bottom = start[1]
            room_sprite.player_sprite.left = left
            room_sprite.player_sprite.bottom = bottom
            room_sprite.player_list.append(room_sprite.player_sprite)


            # add next room portal
            end = current_room.next_level
            sprite = arcade.Sprite("image/bush.png", .15)
            left = end[0]
            bottom = end[1]
            sprite.left = left
            sprite.bottom = bottom
            room_sprite.next_level.append(sprite)

            # add coins
            coins = current_room.coins
            for coin in coins:
                sprite = arcade.Sprite("image/coin.png", .15)
                left = coin[0]
                bottom = coin[1]
                sprite.left = left
                sprite.bottom = bottom
                room_sprite.coin_list.append(sprite)

            # add monster
            monsters = current_room.monsters
            for monster in monsters:
                sprite = arcade.Sprite("image/monster.png", .15)
                left = monster[0]
                bottom = monster[1]
                sprite.left = left
                sprite.bottom = bottom
                room_sprite.monster_list.append(sprite)

            # add walls
            coordinates = current_room.walls
            for coordinate in coordinates:
                wall = arcade.Sprite("image/wall.png", .25)
                left = coordinate[0]
                bottom = coordinate[1]
                wall.left = left
                wall.bottom = bottom
                room_sprite.wall_list.append(wall)

            self.rooms.append(room_sprite)
