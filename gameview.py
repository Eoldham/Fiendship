import arcade
from Player import *
from Levels import *
from Room import *

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 800
BACKGROUND_COLOR = arcade.color.BLACK
GAME_TITLE = "Fiendship"


class GameView(arcade.View):
    def __init__(self):
        super().__init__()

        # sprite lists
        self.wall_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()

        self.player = Player()
        # list of Rooms
        self.all_rooms = allLevels()
        self.all_rooms.create_rooms()

        self.current_room = self.all_rooms.rooms[0]

        # add player
        self.player = Player()
        start = self.current_room.player_start
        for s in start:
            player = arcade.Sprite("image/player.png", .25)
            left = s[0]
            bottom = s[1]
            player.left = left
            player.bottom = bottom
            self.player_list.append(player)

        # add coins
        coins = self.current_room.coins
        for coin in coins:
            sprite = arcade.Sprite("image/coin.png", .15)
            left = coin[0]
            bottom = coin[1]
            sprite.left = left
            sprite.bottom = bottom
            self.wall_list.append(sprite)

        # add walls
        coordinates = self.current_room.coordinates
        for coordinate in coordinates:
            wall = arcade.Sprite("image/wall.png", .25)
            left = coordinate[0]
            bottom = coordinate[1]
            wall.left = left
            wall.bottom = bottom
            self.wall_list.append(wall)

    def on_show(self):
        arcade.set_background_color(BACKGROUND_COLOR)

    def on_draw(self):
        arcade.start_render()
        self.wall_list.draw()
        self.player_list.draw()

    def on_update(self, delta_time):
        pass
