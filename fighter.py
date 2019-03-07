import arcade
import os
import math

FACE_RIGHT = 1
FACE_LEFT = 2
FACE_UP = 3
FACE_DOWN = 4

class Fighter(arcade.Sprite):
    def __init__(self, scale: float=1,
                 image_x: float=0, image_y: float=0,
                 center_x: float=0, center_y: float=0):
        super().__init__(scale=scale, image_x=image_x, image_y=image_y,
                         center_x=center_x, center_y=center_y)
        self.state = FACE_RIGHT
        self.stand_right = None
        self.stand_left = None
        self.walk_left = None
        self.walk_right = None
        self.run_right = None
        self.run_left = None
        self.dead_right = None
        self.dead_left = None
        self.cur_index = 0
        self.delta_distance = 20
        self.prev_center_x = 0
        self.prev_center_y = 0
        self.run = False
        self.dead = False
        self.count = 0

    def update_animation(self):
        if self.dead:
            self.dead_animation()
        else:
            if self.run:
                self.run_animation()
            else:
                self.walk_animation()

    def dead_animation(self):
        texture_list = []
        if self.count >= 17:
            if self.state == FACE_LEFT:
                texture_list = self.dead_left
                if texture_list is None or len(texture_list) == 0:
                    raise RuntimeError("update_animation was called on a sprite that doesn't have a "
                                       "list of walk left textures.")
            elif self.state == FACE_RIGHT:
                texture_list = self.dead_right
                if texture_list is None or len(texture_list) == 0:
                    raise RuntimeError("update_animation was called on a sprite that doesn't have a list of "
                                       "walk right textures.")
            self.cur_index += 1
            if self.cur_index >= len(texture_list):
                self.cur_index = 0
                self.dead = False
            self.count = 0
            self._texture = texture_list[self.cur_index]

        self.width = self._texture.width * self.scale
        self.height = self._texture.height * self.scale
        self.count += 5

    def run_animation(self):
        x1 = self.center_x
        x2 = self.prev_center_x
        y1 = self.center_y
        y2 = self.prev_center_y
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        texture_list = []

        change_direction = False
        if self.change_x > 0 \
                and self.change_y == 0 \
                and self.state != FACE_RIGHT \
                and self.run_right \
                and len(self.run_right) > 0:
            self.state = FACE_RIGHT
            change_direction = True
        elif self.change_x < 0 and self.change_y == 0 and self.state != FACE_LEFT \
                and self.run_left and len(self.run_left) > 0:
            self.state = FACE_LEFT
            change_direction = True

        if self.change_x == 0 and self.change_y == 0:
            if self.state == FACE_LEFT:
                self._texture = self.stand_left[0]
            elif self.state == FACE_RIGHT:
                self._texture = self.stand_right[0]

        elif change_direction or distance >= (self.delta_distance * 2.2):
            self.prev_center_x = self.center_x
            self.prev_center_y = self.center_y

            if self.state == FACE_LEFT:
                texture_list = self.run_left
                if texture_list is None or len(texture_list) == 0:
                    raise RuntimeError("update_animation was called on a sprite that doesn't have a "
                                       "list of walk left textures.")
            elif self.state == FACE_RIGHT:
                texture_list = self.run_right
                if texture_list is None or len(texture_list) == 0:
                    raise RuntimeError("update_animation was called on a sprite that doesn't have a list of "
                                       "walk right textures.")

            self.cur_index += 1
            if self.cur_index >= len(texture_list):
                self.cur_index = 0

            self._texture = texture_list[self.cur_index]

        self.width = self._texture.width * self.scale
        self.height = self._texture.height * self.scale

    def walk_animation(self):
        """
        Logic for selecting the proper texture to use.
        """
        x1 = self.center_x
        x2 = self.prev_center_x
        y1 = self.center_y
        y2 = self.prev_center_y
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        texture_list = []

        change_direction = False
        if self.change_x > 0 \
                and self.change_y == 0 \
                and self.state != FACE_RIGHT \
                and self.walk_right \
                and len(self.walk_right) > 0:
            self.state = FACE_RIGHT
            change_direction = True
        elif self.change_x < 0 and self.change_y == 0 and self.state != FACE_LEFT \
                and self.walk_left and len(self.walk_left) > 0:
            self.state = FACE_LEFT
            change_direction = True

        if self.change_x == 0 and self.change_y == 0:
            if self.state == FACE_LEFT:
                self._texture = self.stand_left[0]
            elif self.state == FACE_RIGHT:
                self._texture = self.stand_right[0]

        elif change_direction or distance >= self.delta_distance:
            self.prev_center_x = self.center_x
            self.prev_center_y = self.center_y

            if self.state == FACE_LEFT:
                texture_list = self.walk_left
                if texture_list is None or len(texture_list) == 0:
                    raise RuntimeError("update_animation was called on a sprite that doesn't have a "
                                       "list of walk left textures.")
            elif self.state == FACE_RIGHT:
                texture_list = self.walk_right
                if texture_list is None or len(texture_list) == 0:
                    raise RuntimeError("update_animation was called on a sprite that doesn't have a list of "
                                       "walk right textures.")

            self.cur_index += 1
            if self.cur_index >= len(texture_list):
                self.cur_index = 0

            self._texture = texture_list[self.cur_index]

        self.width = self._texture.width * self.scale
        self.height = self._texture.height * self.scale
