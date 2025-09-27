import pygame
import global_var
from collision import Collision
from screen_config import Screen
from character_attributes import Atributtes
from life_bar import Life_bar
import sounds

pygame.init()

clock = pygame.time.Clock()

pixel_offset = 10
pixel_offset_y = 10
col_right_offset = 34

pygame.init()


class Megaman(Atributtes, Life_bar, Collision):
    def __init__(self, x, y, health=28, width=14 * 3, height=23 * 3):
        super().__init__(health)
        self.alive = True
        self.mid_transition = False

        self.shooting_offset = 0
        self.y_offset = 0

        self.gravitty = 1
        self.speed = 5
        self.x = x
        self.y = y
        self.init_x = 45
        self.init_y = 400
        self.x_coll = x + pixel_offset
        self.y_coll = y - pixel_offset
        self.width = width
        self.height = height
        self.y_speed = 0

        self.keys_pressed = pygame.key.get_pressed()
        self.moving = False
        self.left = True

        self.animation_index = 0
        self.falling_counter = 1
        self.display_to_blit = Screen.display_screen

        self.onground = True
        self.on_ceiling = False
        self.jumping = False

        self.shooting = False
        self.shoot_timer = 0

        self.on_stair = False
        self.stopped = False
        self.invincible = False
        self.death_timer = 0

        self.walk_sprites = [
            global_var.megaman_sprites["Megaman_Walk_1"],
            global_var.megaman_sprites["Megaman_Walk_2"],
            global_var.megaman_sprites["Megaman_Walk_3"],
            global_var.megaman_sprites["Megaman_Walk_2"],
            global_var.megaman_sprites["Mega_Shoot_walk_1"],
            global_var.megaman_sprites["Mega_Shoot_walk_2"],
            global_var.megaman_sprites["Mega_Shoot_walk_3"],
            global_var.megaman_sprites["Mega_Shoot_walk_2"],
        ]
        self.idle_sprites = [
            global_var.megaman_sprites["Mega_Stand_0"],
            global_var.megaman_sprites["Mega_Shoot_idle"],
        ]

        self.jump_sprites = [
            global_var.megaman_sprites["Mega_Jump"],
            global_var.megaman_sprites["Mega_Shoot_jump"],
        ]

        self.stair_sprite = [
            global_var.megaman_sprites["Megaman_Ladder_1"],
            global_var.megaman_sprites["Mega_Shoot_stair"],
        ]

        self.knockback_sprite = global_var.megaman_sprites["Mega_Pain"]

        self.sprite = self.idle_sprites[0]

        self.character = "megaman"

        self.display_to_blit = Screen.display_screen

        self.collision = self.coll(1)

    def falling(self):
        if not self.on_stair and not self.stopped:
            self.y_speed = self.gravitty * self.falling_counter
            if self.y_speed > 22:
                self.y_speed = 22
            self.vertical_move(pixel_offset_y)
            self.falling_counter += 0.38

    def colliding(self, collision):
        cx = global_var.camera_x
        cy = global_var.camera_y

        colliding = False
        for coll in collision:
            if self.collision.colliderect(coll):
                if not self.on_stair:
                    if (
                        not self.left or (self.stunned and self.left)
                    ) and self.collision.right >= coll.right + col_right_offset:
                        self.collision.left = coll.right + 1
                        self.x = self.collision.left - 12 + cx
                    elif self.collision.right <= coll.left + 2 * self.speed:
                        self.collision.right = coll.left - 1
                        self.x = self.collision.left - 13 + cx

                    elif (
                        self.collision.bottom > coll.top - self.y_speed
                        and self.collision.top < coll.top
                    ):
                        self.onground = True
                        self.y_speed = 0
                        colliding = True
                        self.collision.bottom = coll.top
                        self.y = self.collision.top + cy
                        self.falling_counter = 0
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
                        self.on_stair = False

        if not colliding:
            self.onground = False
            self.falling()

    def on_stair_coll(self, events, stair_collisions):
        cx = global_var.camera_x
        for coll in stair_collisions:
            if self.collision.colliderect(coll):
                if (
                    self.collision.bottom <= coll.top
                    or self.collision.top >= coll.bottom - 20
                ):
                    self.on_stair = False
                for event in events:
                    if (
                        event.type == pygame.KEYDOWN
                        and not self.stunned
                        and (
                            (
                                event.key == pygame.K_w
                                and self.collision.bottom > coll.top + 1
                            )
                            or (
                                event.key == pygame.K_s
                                and self.collision.bottom < coll.bottom + -1
                            )
                        )
                    ):
                        if (
                            self.collision.top < coll.bottom
                            or self.collision.bottom > coll.top
                        ):
                            if (
                                self.collision.bottom + 11 < coll.bottom
                                and not self.on_stair
                            ):
                                self.y += 11
                            self.on_stair = True
                            self.collision.right = coll.left + cx
                            self.x = coll.left + cx
                            self.x_coll = self.x - cx

    def on_death_coll(self, collision):
        for i in range(len(collision) - 1, -1, -1):
            if self.collision.colliderect(collision[i]):
                self.health = 0

    def is_idle(self):
        if not (self.keys_pressed[pygame.K_d] or self.keys_pressed[pygame.K_a]) or (
            self.keys_pressed[pygame.K_a]
            and self.keys_pressed[pygame.K_d]
            or self.stunned
        ):
            self.moving = False
            if not self.on_stair:
                self.animation_index = 0
            self.y_coll = self.y + pixel_offset_y - global_var.camera_y
            self.x_coll = self.x + pixel_offset + 4 - global_var.camera_x

    def move_right(self):
        cy = global_var.camera_y
        if (
            self.keys_pressed[pygame.K_d]
            and self.x - global_var.camera_x < 720 - 58
            and not self.stunned
        ):
            if not self.on_stair:
                self.moving = True
                self.x += self.speed
                self.x_coll = self.x + pixel_offset - global_var.camera_x
            self.left = True
        self.is_idle()
        self.y_coll = self.y + 1 - cy

    def move_left(self):
        cy = global_var.camera_y
        if (
            self.keys_pressed[pygame.K_a]
            and self.x - global_var.camera_x > -10
            and not self.stunned
        ):
            if not self.on_stair:
                self.moving = True
                self.x -= self.speed
                self.x_coll = self.x + pixel_offset - global_var.camera_x + 3
            self.left = False
        self.is_idle()
        self.y_coll = self.y + 1 - cy

    def move_stair(self):
        cx = global_var.camera_x
        if self.on_stair and not self.shooting:
            if self.keys_pressed[pygame.K_w]:
                self.y_speed = -4
                self.moving = True
                self.vertical_move()
            elif self.keys_pressed[pygame.K_s]:
                self.y_speed = 4
                self.moving = True
                self.vertical_move()
            else:
                self.moving = False
            self.x_coll = self.x - cx + 1

    def jump(self):
        if self.onground and not self.stopped:
            self.jumping = True
            if not (self.on_ceiling or self.on_stair):
                self.y_speed -= 15
                self.vertical_move()

    def jumping_state(self):
        if self.onground or self.on_stair:
            self.jumping = False

        if self.jumping:
            cy = global_var.camera_y
            self.y -= 10
            self.y_coll = self.y - cy

    def vertical_move(self, offset=0):
        if not self.stopped:
            self.y += self.y_speed
            self.y_coll = self.y + offset - global_var.camera_y

    def walk_animation(self):
        if self.shooting:
            self.sprite = pygame.transform.flip(
                self.walk_sprites[self.animation_index // (10) + 4], self.left, 0
            )
            if (
                self.animation_index // 10 + 4 == 4
                or self.animation_index // 10 + 4 == 6
            ):
                self.y_offset = -6
            self.shooting_offset = 15 * (not self.left)
        else:
            self.sprite = pygame.transform.flip(
                self.walk_sprites[self.animation_index // 10], self.left, 0
            )
        self.is_idle()
        self.animation_index += 1

    def idle_animation(self):
        if self.shooting:
            self.sprite = pygame.transform.flip(self.idle_sprites[1], self.left, 0)
            self.shooting_offset = 30 * (not self.left)
        else:
            self.sprite = pygame.transform.flip(self.idle_sprites[0], not self.left, 0)

    def falling_animation(self):
        if self.shooting:
            self.sprite = pygame.transform.flip(self.jump_sprites[1], self.left, 0)
            self.shooting_offset = 9 * (not self.left)
        else:
            self.sprite = pygame.transform.flip(self.jump_sprites[0], self.left, 0)

    def stair_animation(self):
        if self.shooting:
            self.sprite = pygame.transform.flip(self.stair_sprite[1], self.left, 0)
            self.shooting_offset = 24 * (not self.left)
        else:
            if self.animation_index <= 10 or 20 < self.animation_index <= 30:
                self.sprite = self.stair_sprite[0]
            else:
                self.sprite = pygame.transform.flip(self.stair_sprite[0], 1, 0)
            if self.moving:
                self.animation_index += 1

    def stunn_animation(self):
        self.sprite = pygame.transform.flip(self.knockback_sprite, self.left, 0)

    def animations(self):
        if not self.stopped:
            if self.animation_index >= 39:
                self.animation_index = 0
            if self.stunned:
                self.stunn_animation()
            elif self.on_stair:
                self.stair_animation()
            elif self.onground:
                if self.moving:
                    self.walk_animation()
                else:
                    self.idle_animation()
            else:
                self.falling_animation()
        if not self.knockback_inx % 4:
            self.display_to_blit.blit(
                pygame.transform.scale_by(self.sprite.convert_alpha(), 3),
                (
                    self.x - global_var.camera_x - self.shooting_offset,
                    self.y - global_var.camera_y - self.y_offset,
                ),
            )
            self.shooting_offset = 0
            self.y_offset = 0

    def respawn(self):
        if global_var.checkpoint:
            self.init_x = 7267
            self.init_y = -3433
        self.stunned = False
        self.invincible = False
        self.left = True
        self.health = 28
        self.mid_transition = False
        self.alive = True
        global_var.enable_boss = False
        self.x = self.init_x
        self.y = self.init_y
        global_var.camera_x = 0 + 6903 * global_var.checkpoint
        global_var.camera_y = 0 - 3800 * global_var.checkpoint
        pygame.mixer.music.load("./audio/music/Cutman_Stage_Theme.mp3")
        pygame.mixer.music.play(-1)

    def take_damage(self, damage):
        if self.alive and not self.invincible:
            sounds.damage.play()
            self.on_stair = False
            self.health -= damage
            self.invincible = True
            self.stunned = True

    def knockback(self):
        cx = global_var.camera_x
        self.knockback_inx += 10
        if self.stunned:
            self.x += 2 - 4 * self.left
            self.x_coll = self.x - cx
        if self.knockback_inx == 700:
            self.knockback_inx = 0
            self.invincible = False

        if self.knockback_inx == 300:
            self.stunned = False
            self.x += -10 + 20 * (self.left)

    def handle_shoot_timer(self):
        self.shoot_timer += 10
        if self.shoot_timer >= 150:
            self.shooting = False
            self.shoot_timer = 0

    def handle_death(self):
        if self.health <= 0:
            if self.death_timer == 0:
                pygame.mixer.music.stop()
                sounds.death.play()
            self.death_timer += 1
            self.alive = False
            if self.death_timer >= 50:
                self.display_to_blit.fill("black")
                self.mid_transition = True
                global_var.first_door_open = False
                global_var.second_door_open = False

            if self.death_timer == 120:
                self.respawn()
                self.death_timer = 0

    def run(self):
        self.stopped = global_var.stop_time
        self.handle_death()
        if self.invincible:
            self.knockback()
        if self.alive:
            if not self.stopped:
                self.move_left()
                self.move_right()
                self.move_stair()
                self.jumping_state()
            self.animations()
        if self.shooting:
            self.handle_shoot_timer()
        self.collision = self.coll(1)
