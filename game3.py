import arcade
import os
from Room import generate_room


WINDOW_WIDTH = 900
WINDOW_HEIGHT = 800
BACKGROUND_COLOR = arcade.color.BLACK
GAME_TITLE = "Fiendship"


class Fiendship(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)

        # sprite lists
        self.wall_list = None

    def setup(self):
        arcade.set_background_color(BACKGROUND_COLOR)

        self.wall_list = arcade.SpriteList()

        room = generate_room()
        room.choose_size()
        room.create_walls()
        room_width = room.width
        room_height = room.height
        room.add_border()


        coordinates = room.coordinates
        for coordinate in coordinates:
            wall = arcade.Sprite("image/wall.png",.25)
            left = coordinate[0]
            bottom= coordinate[1]
            wall.left = left
            wall.bottom = bottom
            self.wall_list.append(wall)

    def on_draw(self):
        arcade.start_render()
        self.wall_list.draw()

    def on_update(self, delta_time):
        pass


def main():
    window = Fiendship()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
