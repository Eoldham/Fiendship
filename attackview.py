import arcade
from constants import *
from gameview import *
import random
from gameover import *
from purchase import *
from numtostring import *
from playerattack import *
from monsterattack import *


class AttackView(arcade.View):

    def __init__(self, game_view):
        super().__init__()
        self.monster_health = 0
        self.game_view = game_view
        self.sprite_list = None
        self.player_health = self.game_view.player_health
        self.player_coins = self.game_view.player_coins
        self.monster_letter = 0
        self.player_letter = 0
        self.current_room = self.game_view.current_room
        self.whose_attack = True

        # set monsters health
        if 0 <= self.game_view.current_room < 5:
            self.monster_health = random.randint(10, 25)
        if 5 <= self.game_view.current_room < 10:
            self.monster_health = random.randint(25, 50)
        if 10 <= self.game_view.current_room < 15:
            self.monster_health = random.randint(25, 75)
        if 15 <= self.game_view.current_room <= 20:
            self.monster_health = random.randint(25, 100)

    def on_show(self):
        arcade.set_background_color(arcade.color.BROWN_NOSE)

        # create sprites
        self.sprite_list = arcade.SpriteList()

        # figure out monster sprite
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
        bottom = WINDOW_HEIGHT / 2 + 30
        sprite.left = left
        sprite.bottom = bottom
        self.sprite_list.append(sprite)

        sprite2 = arcade.Sprite(image, 1)
        left = 600
        bottom = WINDOW_HEIGHT / 2 + 30
        sprite2.left = left
        sprite2.bottom = bottom
        self.sprite_list.append(sprite2)



    def on_draw(self):
        arcade.start_render()

        self.sprite_list.draw()

        arcade.draw_text("Attack!!",
                         WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2,
                         arcade.color.PINK_LACE, font_size=20, anchor_x="center")
        arcade.draw_text("Press space to attack the vegetable!Then press enter to defend and refresh health !",
                         WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 40,
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
        if key == arcade.key.P:
            purchase = PurchaseView(self)
            self.window.show_view(purchase)
        elif key == arcade.key.SPACE:
            if self.whose_attack:
                player_attack = playerAttack(self)
                self.window.show_view(player_attack)
                self.game_view.player_health = self.player_health
                self.whose_attack = not self.whose_attack
                if self.monster_health <= 0:
                    self.window.show_view(self.game_view)
            else:
                pass
        elif key == arcade.key.ENTER:
            if self.monster_health <= 0:
                self.window.show_view(self.game_view)
            elif not self.whose_attack:
                monster_attack = monsterAttack(self)
                self.window.show_view(monster_attack)
                self.game_view.player_health = self.player_health
                self.whose_attack = not self.whose_attack
        self.game_view.player_health = self.player_health
