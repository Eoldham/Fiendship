import arcade
from constants import *
from gameview import *
import random
from gameover import *


def number_to_string(num):
    letter = ""
    if num == 1:
        letter = "a"
    if num == 2:
        letter = "b"
    if num == 3:
        letter = "c"
    if num == 4:
        letter = "d"
    if num == 5:
        letter = "e"
    if num == 6:
        letter = "f"
    if num == 7:
        letter = "g"
    if num == 8:
        letter = "h"
    if num == 9:
        letter = "i"
    if num == 10:
        letter = "j"
    if num == 11:
        letter = "k"
    if num == 12:
        letter = "l"
    if num == 13:
        letter = "m"
    if num == 14:
        letter = "n"
    if num == 15:
        letter = "o"
    if num == 16:
        letter = "p"
    if num == 17:
        letter = "q"
    if num == 18:
        letter = "r"
    if num == 19:
        letter = "s"
    if num == 20:
        letter = "t"
    if num == 21:
        letter = "u"
    if num == 22:
        letter = "v"
    if num == 23:
        letter = "w"
    if num == 24:
        letter = "x"
    if num == 25:
        letter = "y"
    if num == 26:
        letter = "z"
    return letter


class AttackView(arcade.View):

    def __init__(self, game_view):
        super().__init__()
        self.monster_health = 0
        self.game_view = game_view
        self.number_of_attacks = 0
        self.monster_letter = 0
        self.player_letter = 0
        self.sprite_list = None

    def on_show(self):
        arcade.set_background_color(arcade.color.BROWN_NOSE)

        # set monsters letter:
        self.monster_letter = random.randint(1, 26)

        #create sprites
        self.sprite_list = arcade.SpriteList()

        #figure out monster sprite
        if self.game_view.current_room < 5:
            image = "image/monster.png"
        if 5 <= self.game_view.current_room < 10:
            image = "image/monster2.png"
        if 10 <= self.game_view.current_room < 15:
            image = "image/monster3.png"
        if 15 <= self.game_view.current_room <= 20:
            image = "image/monster4.png"

        sprite = arcade.Sprite("image/player.png", 1)
        left = 100
        bottom = WINDOW_HEIGHT/2 + 30
        sprite.left = left
        sprite.bottom = bottom
        self.sprite_list.append(sprite)

        sprite2 = arcade.Sprite(image, 1)
        left = 600
        bottom = WINDOW_HEIGHT / 2 + 30
        sprite2.left = left
        sprite2.bottom = bottom
        self.sprite_list.append(sprite2)

        # set monsters health
        if 0 <= self.game_view.current_room < 5:
            self.monster_health = random.randint(10, 25)
        if 5 <= self.game_view.current_room < 10:
            self.monster_health = random.randint(25, 75)
        if 10 <= self.game_view.current_room < 15:
            self.monster_health = random.randint(25, 100)
        if 15 <= self.game_view.current_room <= 20:
            self.monster_health = random.randint(25, 150)

    def on_draw(self):
        arcade.start_render()

        self.sprite_list.draw()

        arcade.draw_text("Guess a letter to decide the monsters attack, try to be spot on or exactly five away!",
                         WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2,
                         arcade.color.PINK_LACE, font_size=20, anchor_x="center")
        difference = abs(self.player_letter - self.monster_letter)
        output = f"Monster Health: {self.monster_health}"
        arcade.draw_text(output, 100, 200, arcade.color.PINK_LACE, 20)
        output = f"Player Health: {self.game_view.player_health}"
        arcade.draw_text(output, 600, 200, arcade.color.PINK_LACE, 20)
        output = f"Player Letter: {number_to_string(self.player_letter)}"
        arcade.draw_text(output, 300, 100, arcade.color.PINK_LACE, 20)
        output = f"letters away: {difference}"
        arcade.draw_text(output, 300, 50, arcade.color.PINK_LACE, 20)

    def on_key_press(self, key, modifiers):
        self.monster_attack(key, modifiers)
        self.player_attack()

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

    def player_attack(self):
        self.number_of_attacks += 1
        # player attack
        # Find attack power for player
        attack_power = 0
        bonus = self.get_bonus()
        stamina = self.game_view.player_stamina
        defense = 0

        # monsters defense:
        defense = self.monster_health

        # stamina
        if 0 <= self.game_view.current_room < 5:
            stamina = int(stamina/8)
        if 5 <= self.game_view.current_room < 10:
            stamina = int(stamina/6)
        if 10 <= self.game_view.current_room < 15:
            stamina = int(stamina/4)
        if 15 <= self.game_view.current_room <= 20:
            stamina = int(stamina/4)

        attack_power = stamina + bonus - defense
        self.monster_health = self.monster_health - abs(attack_power) - 1
        # end Attack View
        if self.monster_health <= 0:

            # deplete stamina
            self.game_view.player_stamina = self.game_view.player_stamina - self.number_of_attacks * 5

            # drop item
            item_number = random.randint(1, 3)
            bonus = self.get_bonus()
            if item_number == 1:
                self.game_view.player_health = self.game_view.player_health + bonus
            if item_number == 2:
                self.game_view.player_stamina = self.game_view.player_stamina + bonus
            if item_number == 3:
                self.game_view.player_stamina = self.game_view.player_stamina + bonus
                self.game_view.player_health = self.game_view.player_health + bonus

            monster_letter = number_to_string(self.monster_letter)
            difference = abs(self.player_letter - self.monster_letter)
            # write on screen
            if item_number == 1:
                self.game_view.message = "You have gained health! Monsters Letter: {} You were {} away".format(monster_letter,difference)
            if item_number == 2:
                self.game_view.message = "You have gained stamina! Monsters Letter: {} You were {} away".format(monster_letter,difference)
            if item_number == 3:
                self.game_view.message = "You have gained health and stamina! Monsters letter: {} You were {} away ".format(
                    monster_letter,difference)

            self.window.show_view(self.game_view)

    def monster_attack(self, key, modifiers):
        player_letter = 0
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

        self.player_letter = player_letter

        # check player_letter vs. monster letter
        multiplier = self.game_view.current_room/2
        attack = abs(self.monster_letter - self.player_letter)

        self.game_view.player_health = self.game_view.player_health - attack

        if self.game_view.player_health <= 0:
            dead_view = DeadView()
            self.window.show_view(dead_view)
