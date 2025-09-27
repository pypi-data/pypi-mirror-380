import pygame
import global_var
from screen_config import Screen
from collision import Collision


class Projectile(Collision):
    def __init__(self, direction, x, y, kind, width=5 * 3, height=5 * 3):
        self.sprite = [
            global_var.pj_sprites["Blaster_proj"],
        ]
        self.direction = direction
        self.f_off = 28 * self.direction

        self.x = x - 10 + self.f_off
        self.y = y + 10
        self.width = width
        self.height = height
        self.kind = kind

        self.x_coll = self.x
        self.y_coll = self.y
        self.collision = self.coll(0, 4, 4)

        self.screen_to_blit = Screen.display_screen

    def move_shoot(self, shoots):
        cx = global_var.camera_x
        for i in range(len(shoots) - 1, -1, -1):
            for j in range(70):
                if j % 10 == 0:
                    if -60 + cx < shoots[i].x < 720 + cx:
                        if shoots[i].kind == 1:
                            shoots[i].x -= 2 - 4 * shoots[i].direction
                            shoots[i].y -= 1
                            shoots[i].x_coll = shoots[i].x
                            shoots[i].y_coll = shoots[i].y
                        elif shoots[i].kind == 2:
                            shoots[i].x -= 2 - 4 * shoots[i].direction
                            shoots[i].y -= 0.2
                            shoots[i].x_coll = shoots[i].x
                            shoots[i].y_coll = shoots[i].y
                        elif shoots[i].kind == 3:
                            shoots[i].x -= 2 - 4 * shoots[i].direction
                            shoots[i].y += 0.2
                            shoots[i].x_coll = shoots[i].x
                            shoots[i].y_coll = shoots[i].y
                        elif shoots[i].kind == 4:
                            shoots[i].x -= 2 - 4 * shoots[i].direction
                            shoots[i].y += 1
                            shoots[i].x_coll = shoots[i].x
                            shoots[i].y_coll = shoots[i].y
                    else:
                        shoots.remove(shoots[i])
                        break

    def show(self, shoots):
        cx = global_var.camera_x
        cy = global_var.camera_y
        for i in range(len(shoots) - 1, -1, -1):
            shoots[i].collision = shoots[i].coll(0, 4, 4)
            self.screen_to_blit.blit(
                pygame.transform.scale_by(self.sprite[0], 3),
                (shoots[i].x - cx, shoots[i].y - cy),
            )

    def check_collision(self, enemies, mega, damage=3):
        for i in range(len(enemies) - 1, -1, -1):
            if mega.collision.colliderect(enemies[i].collision):
                mega.take_damage(damage)

    def run_shoots(self, shoots, mega):
        self.show(shoots)
        self.move_shoot(shoots)
        self.check_collision(shoots, mega)
