import arcade
from Player import *
from Levels import *
from Room import *
from constants import *


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
            self.player_sprite = player

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

        # Physics engine
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

    def on_show(self):
        arcade.set_background_color(BACKGROUND_COLOR)

    def on_draw(self):
        arcade.start_render()
        self.wall_list.draw()
        self.player_list.draw()

    def on_key_press(self, key, modifiers):
        # player movements
        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        if key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = - PLAYER_MOVEMENT_SPEED
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = - PLAYER_MOVEMENT_SPEED
        if key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        # player movements
        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        self.physics_engine.update()
