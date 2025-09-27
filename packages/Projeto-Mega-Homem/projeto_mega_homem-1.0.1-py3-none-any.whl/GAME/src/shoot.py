import pygame
import global_var
from screen_config import Screen
from collision import Collision


class Shoot(Collision):
    def __init__(self, x, y, width=6 * 3, height=6 * 3):
        self.shoot_x = x + 60
        self.shoot_y = y + 3
        self.shoot_speed = 12

        self.width = width
        self.height = height
        self.x_coll = self.shoot_x
        self.y_coll = self.shoot_y
        self.collision = self.coll(0, 10, 10)

        self.screen = Screen.display_screen
        self.enable_sprite = False
        self.buster_sprite = [global_var.megaman_sprites["Mega_Buster"]]

    def lemon_shoot(self, shoots, mega):
        if global_var.shoots < 3:
            global_var.shoots += 1
        for i in range(len(shoots) - 1, -1, -1):
            shoots[i][0].enable_sprite = True
        mega.shooting = True
        mega.shoot_timer = 0

    def draw_sprite(self, shoots):
        for i in range(len(shoots) - 1, -1, -1):
            if shoots[i][0].enable_sprite:
                shoots[i][0].collision = shoots[i][0].coll(0, 30, 36)
                self.screen.blit(
                    pygame.transform.scale_by(self.buster_sprite[0], 3),
                    (
                        shoots[i][0].shoot_x - global_var.camera_x,
                        shoots[i][0].shoot_y - global_var.camera_y,
                    ),
                )

    def move_shoot(self, shoots):
        cx = global_var.camera_x
        for i in range(len(shoots) - 1, -1, -1):
            if shoots[i][0].enable_sprite:
                if -60 + cx < shoots[i][0].shoot_x < 720 + cx:
                    shoots[i][0].shoot_x += self.shoot_speed * (
                        1 - 2 * (not shoots[i][1])
                    )
                    shoots[i][0].x_coll = shoots[i][0].shoot_x
                else:
                    shoots[i][0].enable_sprite = False
                    self.delete_shoot(shoots, shoots[i])
                    break

    def delete_shoot(self, shoots, shoot):
        for i in range(len(shoots) - 1, -1, -1):
            if shoots[i] == shoot:
                shoots.remove(shoot)
        global_var.shoots -= 1
        if global_var.shoots < 0:
            global_var.shoots = 0

    def run(self, shoots, mega):
        self.draw_sprite(shoots)
        self.move_shoot(shoots)
