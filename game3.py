import arcade

from Room import generate_room

WINDOW_WIDTH = 800
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

        for x in (0, room_width):
            border = arcade.Sprite("images/wall.png", 1)
            border.center_x = x
            border.center_y = 0
            self.wall_list.append(border)
        for x in (0, room_width):
            border = arcade.Sprite("images/wall.png", 1)
            border.center_x = x
            border.center_y = room_height
            self.wall_list.append(border)
        for y in (0, room_height):
            border = arcade.Sprite("images/wall.png", 1)
            border.center_x = 0
            border.center_y = y
            self.wall_list.append(border)
        for y in (0, room_height):
            border = arcade.Sprite("images/all.png", 1)
            border.center_x = room_width
            border.center_y = y
            self.wall_list.append(border)

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
