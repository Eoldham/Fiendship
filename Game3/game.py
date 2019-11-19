from Game3.Player_sprite import *


class YourGameClassRenameThis(arcade.Window):
    def __init__(self):
        # Initialize variables
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)

        # Sprite lists:
        self.wall_list = None
        self.player_list = None
        self.Player_sprite = None
        self.physics_engine = None

    def setup(self):
        # Setup the game (or reset the game)
        arcade.set_background_color(BACKGROUND_COLOR)

        # set up Sprite lists
        self.wall_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.Player_sprite = Player()
        self.player_list.append(self.Player_sprite)

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.wall_list, self.Player_sprite, GRAVITY)
        # set up Level
        level_name = "Level1.tmx"
        ground_layer_name = 'Wall'
        level1 = arcade.tilemap.read_tmx(level_name)
        self.wall_list = arcade.tilemap.process_layer(level1, ground_layer_name, TILE_SCALING)
        if level1.background_color:
            arcade.set_background_color(level1.background_color)

    def on_draw(self):
        # Called when it is time to draw the world
        arcade.start_render()
        self.wall_list.draw()
        self.player_list.draw()

    def on_update(self, delta_time):
        # Called every frame of the game (1/GAME_SPEED times per second)
        pass

    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.Player_sprite.jump()
            elif key == arcade.key.LEFT or key == arcade.key.A:
                self.Player_sprite.left()
            elif key == arcade.key.RIGHT or key == arcade.key.D:
                self.Player_sprite.right()

    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.W:
            self.Player_sprite.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.Player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.Player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.Player_sprite.change_x = 0

    def on_update(self, delta_time):
        self.physics_engine.update()

def main():
    window = YourGameClassRenameThis()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
