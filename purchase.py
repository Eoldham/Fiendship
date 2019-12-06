import arcade
from gameview import *
from attackview import *
from constants import *


class PurchaseView(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view
        self.sprite_list = arcade.SpriteList()

    def on_show(self):
        arcade.set_background_color(arcade.color.BROWN_NOSE)

        sprite = arcade.Sprite("image/coin.png", 1)
        left = WINDOW_WIDTH / 2 - 100
        bottom = WINDOW_HEIGHT / 2 + 60
        sprite.left = left
        sprite.bottom = bottom
        self.sprite_list.append(sprite)

    def on_draw(self):
        arcade.start_render()

        self.sprite_list.draw()

        arcade.draw_text("Welcome to the Flower Shop!",
                         WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2,
                         arcade.color.PINK_LACE, font_size=40, anchor_x="center")
        arcade.draw_text("Here you can sell 1 flower for 10 Health or 5 Stamina",
                         WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 100,
                         arcade.color.PINK_LACE, font_size=20, anchor_x="center")
        arcade.draw_text("To Buy health you just have to press h",
                         WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 140,
                         arcade.color.PINK_LACE, font_size=20, anchor_x="center")
        arcade.draw_text("To go back press b",
                         WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 180,
                         arcade.color.PINK_LACE, font_size=20, anchor_x="center")
        output = f"Health: {self.game_view.player_health}"
        arcade.draw_text(output, 0, WINDOW_HEIGHT - 20, arcade.color.PINK_LACE, 20)
        output = f"Flowers: {self.game_view.player_coins}"
        arcade.draw_text(output, 0, WINDOW_HEIGHT - 60, arcade.color.PINK_LACE, 20)

    def on_key_press(self, key, modifiers: int):
        if key == arcade.key.S:
            if self.game_view.player_coins == 0:
                self.window.show_view(self.game_view)
            else:
                self.game_view.player_stamina = self.game_view.player_stamina + 5
                self.game_view.player_coins = self.game_view.player_coins - 1
        elif key == arcade.key.H:
            if self.game_view.player_coins == 0:
                self.window.show_view(self.game_view)
            else:
                self.game_view.player_health = self.game_view.player_health + 10
                self.game_view.player_coins = self.game_view.player_coins - 1
        elif key == arcade.key.B:
            self.window.show_view(self.game_view)
        else:
            pass
