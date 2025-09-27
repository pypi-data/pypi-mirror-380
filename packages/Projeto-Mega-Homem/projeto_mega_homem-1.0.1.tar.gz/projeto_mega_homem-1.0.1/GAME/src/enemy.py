import pygame
from random import randint

import global_var
import sounds
from collision import Collision
from screen_config import Screen
from projectile import Projectile


class Enemy(Collision):
    def __init__(self, x, y, width=48, height=48, health=0, damage=2):
        self.x = x
        self.y = y
        self.init_x = self.x
        self.init_y = self.y
        self.width = width
        self.height = height
        self.health = health
        self.max_health = self.health
        self.damage = damage
        self.spawned = False
        self.anim_inx = 0
        self.screen_to_blit = Screen.display_screen
        self.can_respawn = True
        self.attacking = True
        self.defending = False

    def take_damage(self, enemies, shoots):
        for shoot in shoots:
            for enemy in enemies:
                if enemy.collision.colliderect(shoot[0].collision):
                    if not enemy.defending:
                        enemy.health -= 1
                        sounds.enemy_damage.play()
                    else:
                        sounds.reflect_fire.play()
                    shoot[0].delete_shoot(shoots, shoot)

    def check_col(self, enemies, mega):
        for i in range(len(enemies) - 1, -1, -1):
            if mega.collision.colliderect(enemies[i].collision):
                mega.take_damage(enemies[i].damage)

    def in_screen(self, enemies):
        cx = global_var.camera_x
        cy = global_var.camera_y
        for i in range(len(enemies) - 1, -1, -1):
            if (enemies[i].x - cx < -80 or enemies[i].x - cx > 760) or (
                enemies[i].y - cy < 0 or enemies[i].y - cy > 720
            ):
                enemies[i].anim_inx = 0
                enemies[i].project = []
                enemies[i].can_respawn = True
                enemies[i].health = enemies[i].max_health
                enemies[i].x = enemies[i].init_x
                enemies[i].y = enemies[i].init_y
                enemies[i].x_coll = enemies[i].x
                enemies[i].y_coll = enemies[i].y
                enemies[i].collision = self.coll()
                enemies.remove(enemies[i])

    def check_health(self, enemies):
        for i in range(len(enemies) - 1, -1, -1):
            if enemies[i].health == 0:
                enemies[i].can_respawn = True
                enemies[i].x = enemies[i].init_x
                enemies[i].y = enemies[i].init_y
                enemies[i].x_coll = enemies[i].x
                enemies[i].y_coll = enemies[i].y
                enemies.remove(enemies[i])


class Blaster(Enemy, Projectile):
    def __init__(
        self, x=0, y=0, direction=True, width=9 * 3, height=16 * 3, health=1, damage=1
    ):
        super().__init__(
            x,
            y,
            width,
            height,
            health,
            damage,
        )
        self.damage = damage
        self.direction = direction
        self.fv = 28 * self.direction  # flip value

        self.x_coll = self.x - 48 * self.direction
        self.y_coll = self.y

        self.sprites = [
            global_var.blaster_sprites["Blaster_0"],
            global_var.blaster_sprites["Blaster_Attack_0"],
            global_var.blaster_sprites["Blaster_Attack_1"],
            global_var.blaster_sprites["Blaster_Attack_2"],
            global_var.blaster_sprites["Blaster_Attack_1"],
            global_var.blaster_sprites["Blaster_Attack_0"],
        ]
        self.active_sprite = pygame.transform.scale_by(
            self.sprites[0].convert_alpha(), 3
        )

        self.collision = self.coll()

        self.defending = False
        self.project = []

    def animation(self, enemies):
        cx = global_var.camera_x
        cy = global_var.camera_y
        for i in range(len(enemies) - 1, -1, -1):
            if enemies[i].anim_inx == 270:
                enemies[i].anim_inx = 0

            elif enemies[i].anim_inx == 245:
                enemies[i].active_sprite = pygame.transform.scale_by(
                    enemies[i].sprites[0].convert_alpha(), 3
                )
                enemies[i].defending = True

            elif enemies[i].anim_inx == 230:
                enemies[i].active_sprite = pygame.transform.scale_by(
                    enemies[i].sprites[1].convert_alpha(), 3
                )

            elif enemies[i].anim_inx == 215:
                enemies[i].active_sprite = pygame.transform.scale_by(
                    enemies[i].sprites[2].convert_alpha(), 3
                )

            elif enemies[i].anim_inx == 200:
                enemies[i].attack(enemies[i], 4)

            elif enemies[i].anim_inx == 150:
                enemies[i].attack(enemies[i], 3)

            elif enemies[i].anim_inx == 100:
                enemies[i].attack(enemies[i], 2)

            elif enemies[i].anim_inx == 50:
                enemies[i].active_sprite = pygame.transform.scale_by(
                    enemies[i].sprites[3].convert_alpha(), 3
                )
                enemies[i].collision = enemies[i].coll(0, -5 * 3 + enemies[i].fv)
                enemies[i].attack(enemies[i], 1)

            elif enemies[i].anim_inx == 35:
                enemies[i].active_sprite = pygame.transform.scale_by(
                    enemies[i].sprites[2].convert_alpha(), 3
                )

            elif enemies[i].anim_inx == 20:
                enemies[i].active_sprite = pygame.transform.scale_by(
                    enemies[i].sprites[1].convert_alpha(), 3
                )
                enemies[i].defending = False

            elif enemies[i].anim_inx == 15:
                enemies[i].active_sprite = pygame.transform.scale_by(
                    enemies[i].sprites[0].convert_alpha(), 3
                )

            enemies[i].collision = enemies[i].coll(0, 20 + enemies[i].fv)
            enemies[i].anim_inx += 1
            enemies[i].screen_to_blit.blit(
                pygame.transform.flip(
                    enemies[i].active_sprite, enemies[i].direction, 0
                ),
                (enemies[i].x - cx, enemies[i].y - cy),
            )

    def attack(self, enemy, kind):
        proj = Projectile(enemy.direction, enemy.x, enemy.y, kind)
        enemy.project.append(proj)
        sounds.enemy_fire.play()

    def run_proj(self, enemies, obj_bull, mega):
        for i in range(len(enemies) - 1, -1, -1):
            obj_bull.run_shoots(enemies[i].project, mega)

    def run(self, enemies, obj_bull, shoots, mega):
        for enemy in enemies:
            enemy.can_respawn = False
        self.in_screen(enemies)
        self.check_health(enemies)
        self.take_damage(enemies, shoots)
        self.animation(enemies)
        self.run_proj(enemies, obj_bull, mega)
        self.check_col(enemies, mega)


class Helicopter(Enemy):
    def __init__(self, x=600, y=0, width=13 * 3, height=15 * 3, health=1, damage=3):
        super().__init__(
            x,
            y,
            width,
            height,
            health,
            damage,
        )
        self.x_coll = self.x
        self.y_coll = self.y
        self.sprites = [
            global_var.helicopter_sprites["Fly_1"],
            global_var.helicopter_sprites["Fly_2"],
        ]
        self.used_sprite = pygame.transform.scale_by(self.sprites[0].convert_alpha(), 3)

        self.collision = self.coll(0)

        self.direction = False

        self.attacking = False
        self.target = self.y

    def animation(self, bundy):
        cx = global_var.camera_x
        cy = global_var.camera_y
        for i in range(len(bundy)):
            if bundy[i].anim_inx == 7:
                bundy[i].anim_inx = 0
            if bundy[i].anim_inx == 3:
                bundy[i].used_sprite = self.sprites[1].convert_alpha()
                bundy[i].used_sprite = pygame.transform.scale_by(
                    bundy[i].used_sprite, 3
                )
                bundy[i].screen_to_blit.blit(
                    bundy[i].used_sprite, (bundy[i].x - cx, bundy[i].y - cy)
                )
            if bundy[i].anim_inx == 6:
                bundy[i].used_sprite = self.sprites[0].convert_alpha()
                bundy[i].used_sprite = pygame.transform.scale_by(
                    bundy[i].used_sprite, 3
                )
            bundy[i].screen_to_blit.blit(
                bundy[i].used_sprite, (bundy[i].x - cx, bundy[i].y - cy)
            )
            bundy[i].anim_inx += 1

    def move(self, enemies):
        cx = global_var.camera_x
        for i in range(len(enemies)):
            if enemies[i].x >= 720 + cx:
                enemies[i].direction = False
            if enemies[i].x <= -50 + cx:
                enemies[i].direction = True
            if enemies[i].direction:
                enemies[i].x += 4
                enemies[i].x_coll += 4
            else:
                enemies[i].x -= 4
                enemies[i].x_coll -= 4
            enemies[i].collision = enemies[i].coll(0, 5, 10)

    def attack(self, enemies, mega_x, mega_y):
        for i in range(len(enemies)):
            if (
                mega_x - 100 < enemies[i].x < mega_x + 100
                and mega_y - 210 < enemies[i].y < mega_y + 210
            ):
                if not enemies[i].attacking:
                    enemies[i].attacking = True
                    enemies[i].target = 1

                if (
                    enemies[i].attacking
                    and not enemies[i].direction
                    and mega_x < enemies[i].x < mega_x + 100
                ):
                    enemies[i].down(mega_y)
                elif not enemies[i].direction and mega_x - 100 < enemies[i].x < mega_x:
                    enemies[i].up()

                if enemies[i].direction and mega_x - 100 < enemies[i].x < mega_x:
                    enemies[i].down(mega_y)
                elif enemies[i].direction and mega_x < enemies[i].x < mega_x + 100:
                    enemies[i].up()

    def down(self, mega_y):
        if self.y - 7 > mega_y:
            self.y -= 7
        elif self.y + 7 < mega_y:
            self.y += 7
        self.y_coll = self.y

    def up(self):
        if self.y - 7 > self.target:
            self.y -= 7
        elif self.y + 7 < self.target:
            self.y += 7
        self.y_coll = self.y

    def respawn_bunby(self, segment, rand_enemies):
        spawn_x = global_var.camera_x
        spawn_y = global_var.camera_y
        if (
            segment == "Cutman_Stage_Segment_1"
            or segment == "Cutman_Stage_Segment_3"
            or segment == "Cutman_Stage_Segment_5"
            or segment == "Cutman_Stage_Segment_6"
        ) and len(rand_enemies) < 5:
            rand_enemies.append(Helicopter(720 + spawn_x, randint(100, 600) + spawn_y))
        return rand_enemies

    def delete(self, enemies):
        cx = global_var.camera_x
        cy = global_var.camera_y
        for i in range(len(enemies) - 1, -1, -1):
            if (
                enemies[i].x - cx < -80
                or enemies[i].x - cx > 760
                or enemies[i].y - cy < -30
                or enemies[i].y - cy > 740
                or enemies[i].health == 0
            ):
                enemies.remove(enemies[i])

    def run(self, enemies, shoots, mega):
        self.delete(enemies)
        self.animation(enemies)
        self.take_damage(enemies, shoots)
        self.move(enemies)
        self.attack(enemies, mega.x, mega.y)
        self.check_col(enemies, mega)


class Octopus(Enemy):
    def __init__(
        self, x=0, y=0, direction=False, way=False, width=16 * 3, health=3, damage=3
    ):
        super().__init__(x, y, width, health, damage)

        self.direction = direction
        self.way = way
        self.speed = 0

        self.x_coll = self.x
        self.y_coll = self.y

        self.sprites = [
            global_var.octopus_sprites["Octopus_Sleep"],
            global_var.octopus_sprites["Octopus_Move"],
        ]

        self.active_sprite = pygame.transform.scale_by(
            self.sprites[0].convert_alpha(), 3
        )

        self.height = self.width
        self.collision = self.coll()
        self.moving = False
        self.can_move = False

        self.attacking = True
        self.teste = True

    def animation(self, enemies):
        cx = global_var.camera_x
        cy = global_var.camera_y
        for i in range(len(enemies) - 1, -1, -1):
            enemies[i].collision = enemies[i].coll()
            if enemies[i].can_move:
                enemies[i].active_sprite = pygame.transform.scale_by(
                    enemies[i].sprites[1].convert_alpha(), 3
                )
            else:
                enemies[i].active_sprite = pygame.transform.scale_by(
                    enemies[i].sprites[0].convert_alpha(), 3
                )
            enemies[i].screen_to_blit.blit(
                enemies[i].active_sprite, (enemies[i].x - cx, enemies[i].y - cy)
            )

    def move(self, octopus):
        if octopus.direction:
            if octopus.way:
                octopus.speed = -8
            else:
                octopus.speed = 8
            octopus.y += octopus.speed
            octopus.y_coll = octopus.y
        else:
            if octopus.way:
                octopus.speed = 8
            else:
                octopus.speed = -8
            octopus.x += octopus.speed
            octopus.x_coll = octopus.x

    def stop(self, enemies, stage_col):
        cx = global_var.camera_x
        cy = global_var.camera_y
        for i in range(len(enemies) - 1, -1, -1):
            for collision in stage_col:
                if enemies[i].collision.colliderect(collision):
                    if not enemies[i].direction:
                        if (
                            enemies[i].collision.left < collision.right
                            and enemies[i].collision.right > collision.right
                        ):
                            enemies[i].collision.left = collision.right
                            enemies[i].x = enemies[i].collision.left + cx
                            enemies[i].x_coll = enemies[i].x
                        else:
                            enemies[i].collision.right = collision.left
                            enemies[i].x = enemies[i].collision.left + cx
                            enemies[i].x_coll = enemies[i].x
                        if enemies[i].way:
                            enemies[i].way = False
                        else:
                            enemies[i].way = True
                        enemies[i].can_move = False
                    else:
                        if (
                            enemies[i].collision.top < collision.top
                            and enemies[i].collision.bottom < collision.bottom
                        ):
                            enemies[i].collision.bottom = collision.top
                            enemies[i].y = enemies[i].collision.top + cy
                            enemies[i].y_coll = enemies[i].y
                        else:
                            enemies[i].collision.top = collision.bottom
                            enemies[i].y = enemies[i].collision.top + cy
                            enemies[i].y_coll = enemies[i].y
                        if enemies[i].way:
                            enemies[i].way = False
                        else:
                            enemies[i].way = True
                        enemies[i].can_move = False

    def change_way(self, enemies):
        for i in range(len(enemies) - 1, -1, -1):
            if enemies[i].can_move:
                enemies[i].can_move = False
            else:
                enemies[i].can_move = True

    def run(self, enemies, stage_col, shoots, dt, mega):
        for i in range(len(enemies) - 1, -1, -1):
            enemies[i].can_respawn = False
        self.in_screen(enemies)
        self.check_health(enemies)
        self.take_damage(enemies, shoots)
        self.animation(enemies)
        self.stop(enemies, stage_col)
        for i in range(len(enemies) - 1, -1, -1):
            if enemies[i].can_move:
                self.move(enemies[i])
        if dt == 2:
            self.change_way(enemies)
        self.check_col(enemies, mega)


class Big_eye(Enemy):
    def __init__(self, x, y, width=48, height=48 * 3, health=30, damage=7):
        super().__init__(x, y, width, height, health, damage)

        self.x_coll = self.x
        self.y_coll = self.y
        self.health = 30

        self.sprites = [
            global_var.bigeye_sprites["Grounded"],
            global_var.bigeye_sprites["Jump"],
        ]
        self.used_spr = self.sprites[1]

        self.direction = False  # False is Left, True is Right
        self.collision = self.coll()

        self.speed = 0
        self.y_speed = 0

        self.attacking = True
        self.defending = False

        self.jumping = False
        self.on_ground = True

        self.jump_indx = 0
        self.gravity = 1
        self.falling_mult = 0

        self.target = 0
        self.colliding = False
        self.can_respawn = True

    def collision_check(self, enemies, stage_collision):
        cx = global_var.camera_x
        cy = global_var.camera_y
        for i in range(len(enemies) - 1, -1, -1):
            enemies[i].colliding = False
            for coll in stage_collision:
                if enemies[i].collision.colliderect(coll):
                    if (
                        not enemies[i].direction
                        and enemies[i].collision.right >= coll.right + 34
                    ):
                        enemies[i].collision.left = coll.right + 1
                        enemies[i].x = enemies[i].collision.left - 12 + cx
                    elif (
                        enemies[i].direction
                        and enemies[i].collision.right
                        <= coll.left + enemies[i].speed + 34
                    ):
                        enemies[i].collision.right = coll.left
                        enemies[i].x = enemies[i].collision.left - 34 + cx

                    elif (
                        enemies[i].collision.bottom > coll.top - enemies[i].y_speed
                        and enemies[i].collision.top < coll.top
                    ):
                        enemies[i].on_ground = True
                        enemies[i].falling_mult = 0
                        enemies[i].y_speed = 0
                        enemies[i].colliding = True
                        enemies[i].collision.bottom = coll.top + 5
                        enemies[i].y = enemies[i].collision.top + cy
                        enemies[i].jumping = False
                    elif (
                        enemies[i].collision.top < coll.bottom + enemies[i].y_speed
                        and enemies[i].collision.bottom > coll.bottom
                    ):
                        enemies[i].jumping = False
                        enemies[i].collision.top = coll.bottom
                        enemies[i].y = enemies[i].collision.top + cy

                    else:
                        if enemies[i].collision.top + 55 <= coll.top:
                            enemies[i].x -= 8
            enemies[i].x_coll = enemies[i].x
            enemies[i].y_coll = enemies[i].y
            if not enemies[i].colliding:
                enemies[i].on_ground = False
                self.falling(enemies[i])

    def follow(self, enemies, megaman):
        for i in range(len(enemies) - 1, -1, -1):
            enemies[i].jump_indx += 1
            if not enemies[i].jumping:
                enemies[i].target = megaman.x
                if enemies[i].target > enemies[i].x:
                    enemies[i].direction = True
                else:
                    enemies[i].direction = False
            if enemies[i].jump_indx >= 50:
                if not enemies[i].jumping:
                    self.jump(enemies[i])
                enemies[i].speed = -5 + 10 * enemies[i].direction
                enemies[i].x += enemies[i].speed

            if (
                enemies[i].jump_indx > 50
                and enemies[i].jumping
                and enemies[i].on_ground
            ):
                sounds.landing.play()
                enemies[i].y_speed = 0
                enemies[i].jump_indx = 0

    def jump(self, enem):
        enem.jumping = True
        enem.y_speed -= 8
        self.vertical_move(enem)

    def falling(self, enem):
        enem.jumping = True
        enem.falling_mult += 0.025
        if enem.y_speed < 10:
            enem.y_speed += enem.gravity * enem.falling_mult
        self.vertical_move(enem)

    def vertical_move(self, enem):
        enem.y += enem.y_speed

    def animation(self, enemies):
        cx = global_var.camera_x
        cy = global_var.camera_y
        for i in range(len(enemies) - 1, -1, -1):
            if enemies[i].jumping:
                self.jump_animation(enemies[i])
            else:
                enemies[i].used_spr = enemies[i].sprites[0]
                enemies[i].collision = enemies[i].coll(
                    0, 36 * enemies[i].direction, 24, 0, 0
                )
            self.screen_to_blit.blit(
                pygame.transform.scale_by(
                    pygame.transform.flip(enemies[i].used_spr, enemies[i].direction, 0),
                    3,
                ),
                (enemies[i].x - cx, enemies[i].y - cy),
            )

    def jump_animation(self, enemy):
        enemy.used_spr = self.sprites[1]
        enemy.collision = enemy.coll(0, 36 * enemy.direction)

    def run(
        self,
        enemies,
        stage_coll,
        shoots,
        megaman,
    ):
        if not global_var.first_door_open:
            for i in range(len(enemies) - 1, -1, -1):
                enemies[i].can_respawn = False
            self.in_screen(enemies)
            self.check_health(enemies)
            if not megaman.stopped:
                self.collision_check(enemies, stage_coll)
                self.take_damage(enemies, shoots)
                self.check_col(enemies, megaman)
                self.follow(enemies, megaman)
            self.animation(enemies)
