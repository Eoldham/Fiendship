import arcade
from Player import *
from Levels import *
from Room import *
from constants import *
from attackview import *


class GameView(arcade.View):
    def __init__(self):
        super().__init__()

        # player
        self.player_coins = 0
        # list of Rooms

        self.current_room = 0
        self.rooms = []
        levels = allLevels()
        levels.create_sprite_rooms()
        self.rooms = levels.rooms


        # Physics engine
        self.physics_engine = arcade.PhysicsEngineSimple(self.rooms[self.current_room].player_sprite, self.rooms[self.current_room].wall_list)

    def on_show(self):
        arcade.set_background_color(BACKGROUND_COLOR)

    def on_draw(self):
        arcade.start_render()
        self.rooms[self.current_room].wall_list.draw()
        self.rooms[self.current_room].coin_list.draw()
        self.rooms[self.current_room].player_list.draw()
        self.rooms[self.current_room].next_level.draw()
        self.rooms[self.current_room].monster_list.draw()

    def on_key_press(self, key, modifiers):
        # player movements
        if key == arcade.key.UP or key == arcade.key.W:
            self.rooms[self.current_room].player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        if key == arcade.key.DOWN or key == arcade.key.S:
            self.rooms[self.current_room].player_sprite.change_y = - PLAYER_MOVEMENT_SPEED
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.rooms[self.current_room].player_sprite.change_x = - PLAYER_MOVEMENT_SPEED
        if key == arcade.key.RIGHT or key == arcade.key.D:
            self.rooms[self.current_room].player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        # player stops
        if key == arcade.key.UP or key == arcade.key.W:
            self.rooms[self.current_room].player_sprite.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.rooms[self.current_room].player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.rooms[self.current_room].player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.rooms[self.current_room].player_sprite.change_x = 0

    def on_update(self, delta_time):
        self.physics_engine.update()

        # checks if coin is hit
        coin_hit = arcade.check_for_collision_with_list(self.rooms[self.current_room].player_sprite, self.rooms[self.current_room].coin_list)
        for coin in coin_hit:
            self.player_coins += 1
            coin.remove_from_sprite_lists()

        # checks if monster is hit
        monster_attack = arcade.check_for_collision_with_list(self.rooms[self.current_room].player_sprite, self.rooms[self.current_room].monster_list)
        for monster in monster_attack:
            attack_view = AttackView()
            self.window.show_view(attack_view)
            monster.remove_from_sprite_lists()

        # checks if end point hit
        end = arcade.check_for_collision_with_list(self.rooms[self.current_room].player_sprite, self.rooms[self.current_room].next_level)
        for coordinate in end:
            self.current_room = self.current_room + 1
            self.physics_engine = arcade.PhysicsEngineSimple(self.rooms[self.current_room].player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            coordinate.remove_from_sprite_lists()
