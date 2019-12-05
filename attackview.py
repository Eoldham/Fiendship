import arcade
from constants import *
from gameview import *
import random


class AttackView(arcade.View):

    def __init__(self,game_view):
        super().__init__()
        self.monster_health = 0
        self.game_view = game_view

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

        # set monsters health
        if ROOM_NUMBER <= 5:
            self.monster_health = random.randint(25, 50)
        if 5 < ROOM_NUMBER <= 10:
            self.monster_health = random.randint(30, 100)
        if 10 < ROOM_NUMBER <= 15:
            self.monster_health = random.randint(35,150 )
        if 15 < ROOM_NUMBER <= 20:
            self.monster_health = random.randint(50, 200)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Attack Window", WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2,
                         arcade.color.WHITE, font_size=50, anchor_x="center")

    def on_key_press(self, key, modifiers):
        # attack
        if key == arcade.key.SPACE:
            # Find attack power
            bonus = random.randint(5, 50)
            attack = STAMINA + bonus
            defense = random.randint(0, int(attack/2))
            defense += self.monster_health
            attack -= defense
            self.monster_health = self.monster_health - attack
            #if self.monster_health <= 0:
        if key == arcade.key.ENTER:
            self.window.show_view(self.game_view)


    def on_key_release(self, key, modifiers):
        if key == arcade.key.ENTER:
            # Enemy attack and your defense
            defense = STAMINA + HEALTH
            enemy_attack = random.randint(5, 20) + self.monster_health
            enemy_attack = enemy_attack - defense
            HEALTH = HEALTH - enemy_attack


