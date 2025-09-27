import pygame
from random import randint

import global_var
from enemy import Enemy
from rolling_cutter import Rolling_Cutter
from life_bar import Life_bar


class Cutman(Enemy, Life_bar):
    def __init__(self, x, y, width=48, height=72, max_health=28, damage=6):
        super().__init__(x, y, width, height, damage)
        self.max_health = max_health
        self.health = self.max_health
        self.character = "cutman"
        self.damage = damage

        self.speed = 6
        self.y_speed = 0
        self.falling_mult = 0
        self.direction = False

        self.x_coll = self.x
        self.y_coll = self.y

        self.walking = False
        self.jumping = True
        self.on_ground = True

        self.collision = self.coll(0, 9, 24)
        self.gravity = 1

        self.idle_spr = [
            global_var.cutman_sprites["Cutman_Idle_us"],
            global_var.cutman_sprites["Cutman_Idle_1_us"],
            global_var.cutman_sprites["Cutman_Idle"],
            global_var.cutman_sprites["Cutman_Idle_1"],
        ]

        self.walking_spr = [
            global_var.cutman_sprites["Cutman_Walk_1_us"],
            global_var.cutman_sprites["Cutman_Walk_2_us"],
            global_var.cutman_sprites["Cutman_Walk_3_us"],
            global_var.cutman_sprites["Cutman_Walk_2_us"],
            global_var.cutman_sprites["Cutman_Walk_1"],
            global_var.cutman_sprites["Cutman_Walk_2"],
            global_var.cutman_sprites["Cutman_Walk_3"],
            global_var.cutman_sprites["Cutman_Walk_2"],
        ]

        self.jumping_spr = [
            global_var.cutman_sprites["Cutman_Jump_us"],
            global_var.cutman_sprites["Cutman_Jump"],
        ]

        self.shoot_spr = [
            global_var.cutman_sprites["Cutman_Shoot_1"],
            global_var.cutman_sprites["Cutman_Shoot_2"],
        ]

        self.used_spr = self.idle_spr[0]

        self.with_scissors = True
        self.to_shoot = False
        self.shooting = False
        self.shoot_indx = 0

        self.choice = 1

        self.starting = True
        self.alive = True

    def animation(self):
        cx = global_var.camera_x
        cy = global_var.camera_y

        if self.anim_inx == 39:
            self.anim_inx = 0
        self.anim_inx += 1
        if self.jumping:
            self.jump_animation()
        elif self.walking:
            self.walking_animation()
        elif self.shooting:
            self.shoot_animation()
        else:
            self.idle_animation()
        self.screen_to_blit.blit(
            pygame.transform.scale_by(self.used_spr, 3), (self.x - cx, self.y - cy)
        )

    def coll_check(self, collision, megaman):
        cx = global_var.camera_x
        cy = global_var.camera_y

        colliding = False
        for coll in collision:
            if self.collision.colliderect(coll):
                if not self.direction and self.collision.right >= coll.right + 34:
                    self.collision.left = coll.right + 1
                    self.x = self.collision.left - 12 + cx
                    self.jump(megaman, True)
                elif (
                    self.direction
                    and self.collision.right <= coll.left + self.speed + 34
                ):
                    self.collision.right = coll.left
                    self.x = self.collision.left - 8 + cx

                elif (
                    self.collision.bottom > coll.top - self.y_speed
                    and self.collision.top < coll.top
                ):
                    self.on_ground = True
                    self.falling_mult = 0
                    self.y_speed = 0
                    colliding = True
                    self.collision.bottom = coll.top - 21
                    self.y = self.collision.top + cy
                    self.jumping = False
                    self.change_dir(megaman)
                elif (
                    self.collision.top < coll.bottom + self.y_speed
                    and self.collision.bottom > coll.bottom
                ):
                    self.jumping = False
                    self.collision.top = coll.bottom
                    self.y = self.collision.top + cy

                else:
                    if self.collision.top + 55 <= coll.top:
                        self.x -= 8
        if not colliding:
            self.on_ground = False

        self.y_coll = self.y
        self.x_coll = self.x
        self.collision = self.coll(0, 9, 24)
        if not colliding:
            self.on_ground = False
            self.falling()

    def falling(self):
        self.jumping = True
        self.falling_mult += 0.025
        if self.y_speed < 10:
            self.y_speed += self.gravity * self.falling_mult
        self.vertical_move()

    def jump(self, megaman, spc=False):
        in_range = self.x - 48 * 3 <= megaman.x <= self.x + 48 * 3
        if self.on_ground:
            if in_range or (not in_range and spc):
                self.x += 12
                self.jumping = True
                self.y_speed -= 10
                self.vertical_move()

    def change_dir(self, megaman):
        if self.x < megaman.x - 48 * 4:
            if not self.direction:
                self.choice = randint(0, 2)
            self.direction = True
        elif self.x > megaman.x + 48 * 4:
            if self.direction:
                self.choice = randint(0, 2)
            self.direction = False

    def follow(self, megaman):
        if 0 > self.x - global_var.camera_x:
            self.direction = True
        elif self.x - global_var.camera_x > 600:
            self.direction = False
        self.walking = True
        if self.direction:
            self.speed = 5
        else:
            self.speed = -5
        self.x += self.speed
        if self.choice == 2:
            self.jump(megaman)

    def walking_animation(self):
        self.used_spr = pygame.transform.flip(
            self.walking_spr[self.anim_inx // 10 + 4 * self.with_scissors],
            self.direction,
            0,
        )

    def idle_animation(self):
        self.used_spr = pygame.transform.flip(
            self.idle_spr[self.anim_inx // 20 + 2 * self.with_scissors],
            not self.direction,
            0,
        )

    def jump_animation(self):
        if self.jumping:
            self.used_spr = pygame.transform.flip(
                self.jumping_spr[0 + self.with_scissors], self.direction, 0
            )

    def shoot_animation(self):
        if self.shooting:
            self.used_spr = pygame.transform.flip(
                self.shoot_spr[self.anim_inx // 20], not self.direction, 0
            )

    def vertical_move(self):
        self.y += self.y_speed

    def shoot(self, rol_cut, megaman):
        if self.choice == 0:
            self.walking = False
            self.to_shoot = True
            for i in range(100):
                if not i % 10:
                    self.shoot_indx += 1
            if self.shoot_indx == 300:
                self.shooting = True
            if self.shoot_indx == 500:
                self.to_shoot = 0
                self.shooting = 0
                self.choice = randint(1, 2)
                self.shoot_indx = 0
                rol_cut.append(
                    Rolling_Cutter(
                        self.direction,
                        self.x - 30 + 60 * self.direction,
                        self.y + 15,
                        (megaman.x + 30, megaman.y + 30),
                    )
                )
                self.with_scissors = False

    def life_check(self):
        if self.health <= 0:
            self.alive = False

    def restart(self, megaman):
        if megaman.mid_transition:
            self.x = 9813
            self.y = -3333
            self.health = self.max_health
            self.starting = True

    def __on_startup__(self):
        self.starting = False
        pygame.mixer.music.load("./audio/music/Boss_Theme.mp3")
        pygame.mixer.music.play(-1)

    def run(self, boss, rol_cut, floor_collision, megaman, shoots):
        if self.starting:
            self.__on_startup__()
        self.restart(megaman)
        self.life_check()
        if len(rol_cut) == 0:
            self.shoot(rol_cut, megaman)
        if not self.to_shoot:
            self.follow(megaman)
        self.coll_check(floor_collision, megaman)
        self.check_col(boss, megaman)
        self.in_screen(boss)
        self.take_damage(boss, shoots)
        self.animation()
        self.display_health()
