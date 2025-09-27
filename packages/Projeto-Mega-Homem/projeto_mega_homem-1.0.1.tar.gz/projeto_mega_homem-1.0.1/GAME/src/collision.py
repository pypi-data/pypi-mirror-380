import pygame
import global_var


class Collision:
    def __init__(self, name, x_coll, y_coll, width, height):
        self.object = name
        self.x_coll = x_coll
        self.y_coll = y_coll
        self.width = width
        self.height = height

    def coll(self, megaman=0, offset_x=0, offset_y=0, offset_width=0, offset_height=0):
        if not megaman:
            cx = global_var.camera_x
            cy = global_var.camera_y
        else:
            cx = 0
            cy = 0
        return pygame.Rect(
            self.x_coll + offset_x - cx,
            self.y_coll + offset_y - cy,
            self.width + offset_width,
            self.height + offset_height,
        )
