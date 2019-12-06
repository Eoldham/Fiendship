import arcade
from constants import *
from gameview import *
from attackview import *
import random
from monsterattack import *


class playerAttack(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view
        self.plant_a = 0
        self.plant_b = 0
        self.plant_c = 0
        self.sprite_list = arcade.SpriteList()

    def on_show(self):
        arcade.set_background_color(arcade.color.BROWN_NOSE)

        sprite = arcade.Sprite("image/planta.png", 1)
        left = 100
        bottom = 20
        sprite.left = left
        sprite.bottom = bottom
        self.sprite_list.append(sprite)

        sprite = arcade.Sprite("image/plantb.png", 1)
        left = 300
        bottom = 20
        sprite.left = left
        sprite.bottom = bottom
        self.sprite_list.append(sprite)

        sprite = arcade.Sprite("image/plantc.png", 1)
        left = 500
        bottom = 20
        sprite.left = left
        sprite.bottom = bottom
        self.sprite_list.append(sprite)

        self.plants_attack()

    def on_draw(self):
        arcade.start_render()

        self.sprite_list.draw()

        arcade.draw_text("Player Attack", WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 100,
                         arcade.color.PINK_LACE, font_size=50, anchor_x="center")
        arcade.draw_text("Each plant below has an attack", WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 50,
                         arcade.color.PINK_LACE, font_size=20, anchor_x="center")
        arcade.draw_text("Choose the the plant you believe will have the best attack ", WINDOW_WIDTH / 2,
                         WINDOW_HEIGHT / 2,
                         arcade.color.PINK_LACE, font_size=20, anchor_x="center")
        arcade.draw_text("Press a for first plant, b for second plant and c for third plant", WINDOW_WIDTH / 2,
                         WINDOW_HEIGHT / 2 - 30,
                         arcade.color.PINK_LACE, font_size=20, anchor_x="center")

    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.A:
            self.game_view.monster_health = self.game_view.monster_health - self.plant_a
            self.window.show_view(self.game_view)
        elif key == arcade.key.B:
            self.game_view.monster_health = self.game_view.monster_health - self.plant_b
            self.window.show_view(self.game_view)
        elif key == arcade.key.C:
            self.game_view.monster_health = self.game_view.monster_health - self.plant_c
            self.window.show_view(self.game_view)
        else:
            pass

    def plants_attack(self):
        bonus = self.get_bonus()
        self.plant_a = random.randint(5, 20) + bonus
        self.plant_b = random.randint(5, 20) + bonus
        self.plant_c = random.randint(5, 20) + bonus

    def get_bonus(self):
        bonus = 10
        if 0 <= self.game_view.current_room < 5:
            bonus = 0
        if 5 <= self.game_view.current_room < 10:
            bonus = 10
        if 10 <= self.game_view.current_room < 15:
            bonus = 20
        if 15 <= self.game_view.current_room <= 20:
            bonus = 30

        return bonus
