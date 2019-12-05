import arcade
from Player import *
from Levels import *
from Room import *
from constants import *
from attackview import *


class GameView(arcade.View):
    def __init__(self):
        super().__init__()

        # sprite lists
        self.wall_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.monster_list = arcade.SpriteList()
        self.end_sprite_list = arcade.SpriteList()

        # player
        self.player_coins = 0
        self.player_sprite = None
        # list of Rooms
        self.all_rooms = allLevels()
        self.all_rooms.create_rooms()
        self.current_room = 0
        self.rooms = self.all_rooms.rooms
        self.spriteRooms = []
        # add player
        start = self.rooms[self.current_room].player_start
        self.player_sprite = arcade.Sprite("image/player.png", .15)
        left = start[0]
        bottom = start[1]
        self.player_sprite.left = left
        self.player_sprite.bottom = bottom
        self.player_list.append(self.player_sprite)

        # add next room portal
        end = self.rooms[self.current_room].next_level
        self.end_sprite = arcade.Sprite("image/bush.png", .15)
        left = end[0]
        bottom = end[1]
        self.end_sprite.left = left
        self.end_sprite.bottom = bottom
        self.end_sprite_list.append(self.end_sprite)

        # add coins
        coins = self.rooms[self.current_room].coins
        for coin in coins:
            sprite = arcade.Sprite("image/coin.png", .15)
            left = coin[0]
            bottom = coin[1]
            sprite.left = left
            sprite.bottom = bottom
            self.coin_list.append(sprite)

        # add monster
        monsters = self.rooms[self.current_room].monsters
        for monster in monsters:
            sprite = arcade.Sprite("image/monster.png", .15)
            left = monster[0]
            bottom = monster[1]
            sprite.left = left
            sprite.bottom = bottom
            self.monster_list.append(sprite)

        # add walls
        coordinates = self.rooms[self.current_room].walls
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
        self.coin_list.draw()
        self.end_sprite_list.draw()
        self.monster_list.draw()

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
        # player stops
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

        # checks if coin is hit
        coin_hit = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in coin_hit:
            self.player_coins += 1
            coin.remove_from_sprite_lists()

        # checks if monster is hit
        monster_attack = arcade.check_for_collision_with_list(self.player_sprite, self.monster_list)
        for monster in monster_attack:
            attack_view = AttackView()
            self.window.show_view(attack_view)
            monster.remove_from_sprite_lists()

        # checks if end point hit
        end = arcade.check_for_collision_with_list(self.player_sprite, self.end_sprite_list)
        for coordinate in end:
            self.current_room = self.current_room + 1
            coordinate.remove_from_sprite_lists()
