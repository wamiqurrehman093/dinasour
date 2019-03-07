import arcade
import os
import math
from fighter import *

WIDTH = 800
HEIGHT = 600

SCALE = 0.5
SPEED = 5

BLUE = arcade.color.ALICE_BLUE

LEFT = arcade.key.LEFT
RIGHT = arcade.key.RIGHT

class Window(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(path)

        self.player = None

    def on_draw(self):
        arcade.start_render()
        self.player.draw()

    def setup(self):
        arcade.set_background_color(BLUE)
        self.player = Fighter()
        self.player.stand_left = []
        self.player.stand_right = []
        self.player.walk_right = []
        self.player.walk_left = []
        self.player.run_right = []
        self.player.run_left = []
        self.player.dead_right = []
        self.player.dead_left = []

        self.player.stand_right.append(arcade.load_texture('images/stand/0.png', scale=SCALE))
        self.player.stand_left.append(arcade.load_texture('images/stand/0.png', scale=SCALE, mirrored=True))

        for i in range(10):
            self.player.walk_right.append(arcade.load_texture('images/walk/' + str(i) + '.png', scale=SCALE))
            self.player.walk_left.append(arcade.load_texture('images/walk/' + str(i) + '.png', scale=SCALE, mirrored=True))

        for i in range(8):
            self.player.run_right.append(arcade.load_texture('images/run/' + str(i) + '.png', scale=SCALE))
            self.player.run_left.append(arcade.load_texture('images/run/' + str(i) + '.png', scale=SCALE, mirrored=True))
            self.player.dead_right.append(arcade.load_texture('images/die/' + str(i) + '.png', scale=SCALE))
            self.player.dead_left.append(arcade.load_texture('images/die/' + str(i) + '.png', scale=SCALE, mirrored=True))

        self.player.delta_distance = 20
        self.player.center_x = WIDTH//2
        self.player.center_y = HEIGHT//2
        self.player.scale = SCALE

    def update(self, delta_time):
        self.player.update()
        self.player.update_animation()

    def on_key_press(self, key, mods):
        if key == RIGHT:
            self.player.change_x = SPEED
        if key == LEFT:
            self.player.change_x = -SPEED
        if key == RIGHT and mods == arcade.key.MOD_SHIFT:
            self.player.change_x = SPEED * 1.5
            self.player.run = True
        if key == LEFT and mods == arcade.key.MOD_SHIFT:
            self.player.change_x = -SPEED * 1.5
            self.player.run = True
        if key == arcade.key.A:
            self.player.dead = True

    def on_key_release(self, key, mods):
        if key == RIGHT or key == LEFT:
            self.player.change_x = 0
            self.player.run = False
        if mods == arcade.key.MOD_SHIFT:
            self.player.run = False
        # if key == arcade.key.A:
        #     self.dead = False

def main():
    window = Window(WIDTH, HEIGHT)
    window.setup()
    arcade.run()

if __name__ == '__main__':
    main()
