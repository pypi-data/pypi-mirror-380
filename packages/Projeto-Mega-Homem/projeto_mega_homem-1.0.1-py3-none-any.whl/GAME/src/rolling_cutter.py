import pygame

import global_var
from projectile import Projectile


class Rolling_Cutter(Projectile):
    def __init__(self, direction, x, y, target, width=14 * 3, height=14 * 3):
        super().__init__(direction, x, y, kind=None)

        self.damage = 7
        self.width = width
        self.height = height
        self.sprite = global_var.cutman_sprites["Rolling_Cutter"]
        self.target = target
        self.going = True
        self.coming_back = False

        self.used_spr = self.sprite
        self.collision = self.coll()

        self.rotation_inx = 0

    def move(self, cutman, projectile):
        if self.going:
            if self.x < self.target[0] - 9:
                self.x += 9
            elif self.x > self.target[0] + 9:
                self.x -= 9
            if self.y > self.target[1] - 9:
                self.y -= 9
            elif self.y < self.target[1] + 9:
                self.y += 9

            if (
                self.target[0] + 9 >= self.x >= self.target[0] - 9
                and self.target[1] - 9 <= self.y <= self.target[1] + 9
            ):
                self.coming_back = True
                self.going = False
        if self.coming_back:
            if self.x < cutman.x - 6:
                self.x += 6
            elif self.x > cutman.x + 6:
                self.x -= 6
            if self.y < cutman.y + 6:
                self.y += 6
            elif self.y > cutman.y - 6:
                self.y -= 6
            if (
                cutman.x - 6 <= self.x <= cutman.x + 6
                and cutman.y - 6 <= self.y <= cutman.y + 6
            ):
                projectile.remove(projectile[0])

        self.x_coll = self.x
        self.y_coll = self.y
        self.collision = self.coll()

    def display_on_screen(self):
        cx = global_var.camera_x
        cy = global_var.camera_y
        self.screen_to_blit.blit(
            pygame.transform.scale_by(self.used_spr, 3),
            (self.x - cx, self.y - cy),
        )

    def rotate(self):
        if self.rotation_inx >= 40:
            self.rotation_inx = 0
        elif self.rotation_inx >= 30:
            self.used_spr = pygame.transform.rotate(self.sprite, -270)
        elif self.rotation_inx >= 20:
            self.used_spr = pygame.transform.rotate(self.sprite, -180)
        elif self.rotation_inx >= 10:
            self.used_spr = pygame.transform.rotate(self.sprite, -90)
        elif self.rotation_inx >= 0:
            self.used_spr = self.sprite
        self.rotation_inx += 3

    def run(self, cutman, projectiles, megaman):
        self.rotate()
        self.display_on_screen()
        self.move(cutman, projectiles)
        self.check_collision(projectiles, megaman, self.damage)
