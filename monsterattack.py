import arcade
from constants import *
from gameview import *
from attackview import *
import random


class monsterAttack(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view

    def on_show(self):
        arcade.set_background_color(arcade.color.BROWN_NOSE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Vegetable Attack", WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 100,
                         arcade.color.PINK_LACE, font_size=50, anchor_x="center")
        arcade.draw_text("To defend yourself against the vegetable you must guess its favorite letter",
                         WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 30,
                         arcade.color.PINK_LACE, font_size=15, anchor_x="center")
        arcade.draw_text("To do that pick a letter on the keyboard", WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2,
                         arcade.color.PINK_LACE, font_size=15, anchor_x="center")
        arcade.draw_text("If you are within 3 letters of its favorite one you will not be hurt", WINDOW_WIDTH / 2,
                         WINDOW_HEIGHT / 2 - 30,
                         arcade.color.PINK_LACE, font_size=15, anchor_x="center")
        arcade.draw_text("If you aren't you will take damage depending on how far away from the letter you are",
                         WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 60,
                         arcade.color.PINK_LACE, font_size=15, anchor_x="center")

    def on_key_press(self, symbol: int, modifiers: int):
        self.monster_attack(symbol, modifiers)

    def monster_attack(self, key, modifiers):
        monster_letter = random.randint(1, 26)
        player_letter = 0
        bonus = self.get_bonus()

        if key == arcade.key.A:
            player_letter = 1
        elif key == arcade.key.B:
            player_letter = 2
        elif key == arcade.key.C:
            player_letter = 3
        elif key == arcade.key.D:
            player_letter = 4
        elif key == arcade.key.E:
            player_letter = 5
        elif key == arcade.key.F:
            player_letter = 6
        elif key == arcade.key.G:
            player_letter = 7
        elif key == arcade.key.H:
            player_letter = 8
        elif key == arcade.key.I:
            player_letter = 9
        elif key == arcade.key.J:
            player_letter = 10
        elif key == arcade.key.K:
            player_letter = 11
        elif key == arcade.key.L:
            player_letter = 12
        elif key == arcade.key.M:
            player_letter = 13
        elif key == arcade.key.N:
            player_letter = 14
        elif key == arcade.key.O:
            player_letter = 15
        elif key == arcade.key.P:
            player_letter = 16
        elif key == arcade.key.Q:
            player_letter = 17
        elif key == arcade.key.R:
            player_letter = 18
        elif key == arcade.key.S:
            player_letter = 19
        elif key == arcade.key.T:
            player_letter = 20
        elif key == arcade.key.U:
            player_letter = 21
        elif key == arcade.key.V:
            player_letter = 22
        elif key == arcade.key.W:
            player_letter = 23
        elif key == arcade.key.X:
            player_letter = 24
        elif key == arcade.key.Y:
            player_letter = 25
        elif key == arcade.key.Z:
            player_letter = 26
        else:
            player_letter = 12

        self.game_view.monster_letter = monster_letter
        self.game_view.player_letter = player_letter

        difference = abs(monster_letter - player_letter)
        if difference <= 3:
            attack = 0
        else:
            attack = difference + bonus

        self.game_view.player_health = self.game_view.player_health - attack

        print(self.game_view.player_health)

        if self.game_view.player_health <= 0:
            dead_view = DeadView()
            self.window.show_view(dead_view)
        else:
            self.window.show_view(self.game_view)

    def get_bonus(self):
        bonus = 10
        if 0 <= self.game_view.current_room < 5:
            bonus = 10
        if 5 <= self.game_view.current_room < 10:
            bonus = 20
        if 10 <= self.game_view.current_room < 15:
            bonus = 30
        if 15 <= self.game_view.current_room <= 20:
            bonus = 40

        return bonus
