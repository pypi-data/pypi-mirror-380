import pygame

import global_var
import sounds
from collision import Collision
from screen_config import Screen


class Door(Collision, Screen):
    def __init__(self, x, y, kind, width=48, height=12 * 16):
        self.x = x + 50
        self.x_coll = self.x
        self.y = y
        self.y_coll = self.y
        self.width = width
        self.height = height
        self.kind = kind

        self.collision = self.coll()
        self.sprite = global_var.stage_sprites["Door"]
        self.screen = self.display_screen

        self.already_open = False
        self.opening = False
        self.anim_inx = 0
        self.open_inx = 0

    def open(self, megaman):
        if not self.already_open and self.collision.colliderect(megaman):
            self.opening = True
            global_var.stop_time = True
            if self.kind:
                global_var.first_door_open = True
                global_var.checkpoint = True
            else:
                global_var.second_door_open = True

    def draw_door(self):
        cx = global_var.camera_x
        cy = global_var.camera_y
        for i in range(2):
            for j in range(16 - self.open_inx):
                self.screen.blit(
                    pygame.transform.scale_by(self.sprite.convert_alpha(), 3),
                    (self.x + 48 * i - cx, self.y + 12 * j - cy),
                )
        self.collision = self.coll()

    def door_anim(self):
        self.anim_inx += 10
        if self.anim_inx == 300:
            self.open_inx += 4
            sounds.door_open.play()
            self.anim_inx = 0
        if self.open_inx == 16:
            self.opening = False
            global_var.stop_time = False
            self.already_open = True

    def run(self, megaman):
        if not megaman.alive:
            self.open_inx = 0
            self.already_open = False
        self.draw_door()
        if self.opening:
            self.door_anim()
        self.open(megaman.collision)
