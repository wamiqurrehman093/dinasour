from variables import *

class Tree(arcade.Sprite):
    def update(self):
        self.change_x = TREE_SPEED
        self.center_x += self.change_x
        if self.center_x < -40:
            self.center_x = random.randrange(WIDTH, WIDTH + 1000)
