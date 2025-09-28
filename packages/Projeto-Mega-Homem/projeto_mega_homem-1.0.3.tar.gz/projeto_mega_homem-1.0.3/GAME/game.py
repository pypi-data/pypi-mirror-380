import pygame
from pygame import mixer

from GAME.src.tittle import tittle_screen
from GAME.src.ending_screen import ending_screen
from GAME.src.megaman import Megaman
from GAME.src.screen_config import Screen
from GAME.src.shoot import Shoot
from GAME.src.enemy import Helicopter, Blaster, Octopus, Big_eye
from GAME.src.cutman import Cutman
from GAME.src.stage import Stage
from GAME.src.projectile import Projectile
import GAME.src.global_var
from GAME.src import camera
from GAME.src import sounds

pygame.init()
mixer.init()


def main():
    pygame.mixer.music.load("./audio/music/Cutman_Stage_Theme.mp3")

    screen = Screen()
    tittle_screen(screen)
    clock = pygame.time.Clock()
    event_timer = pygame.time.Clock()

    timer = 5
    octopus_timer = 2

    running = True

    mega = Megaman(
        45,
        400,
    )
    buster = Shoot(mega.x_coll + 30, mega.y_coll)
    stage = Stage()
    bundy = Helicopter(0, 0)
    blaster = Blaster(0, 0)
    octopus_bat = Octopus(16 * 3 * 14, 21 * 3 * 5, True, False)
    eye = Big_eye(0, 0)
    bullets = Projectile(1, 0, 0, 0)
    cut = Cutman(9813, -3333)

    shoots = []
    random_enemies = []
    enemies_bl = []
    enemies_oct_b = []
    enemies_b_e = []

    boss = []
    rolling_cutter = []

    boss_enabled = 0

    mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    ending_timer = 0

    while running:
        screen.display_screen.fill("#00e8d8")
        stage.change_segment((mega.x, mega.y))
        stage.draw_stage()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if not mega.stunned and event.key == pygame.K_SPACE:
                    mega.jump()
                if (
                    not mega.stunned
                    and mega.alive
                    and not mega.stopped
                    and event.key == pygame.K_j
                    and GAME.src.global_var.shoots < 3
                ):
                    buster_shoot = Shoot(mega.x - 130 * (not mega.left), mega.y - 15)
                    shoots.append((buster_shoot, mega.left))
                    buster.lemon_shoot(shoots, mega)
                    sounds.shoot.play()
                if event.key == pygame.K_p:
                    if GAME.src.global_var.debug_mode is False:
                        GAME.src.global_var.debug_mode = True
                    else:
                        GAME.src.global_var.debug_mode = False
                if event.key == pygame.K_o:
                    if GAME.src.global_var.disable_bunby_spawn is False:
                        GAME.src.global_var.disable_bunby_spawn = True
                    else:
                        GAME.src.global_var.disable_bunby_spawn = False

        k = pygame.key.get_pressed()
        mega.keys_pressed = k

        floor_col = stage.handle_coll()
        stair_col = stage.handle_stair_coll()
        death_col = stage.handle_death_coll()
        mega.colliding(floor_col)
        mega.on_stair_coll(events, stair_col)
        mega.on_death_coll(death_col)

        segment = stage.selected_sprite

        if GAME.src.global_var.enable_boss:
            if len(boss) == 0:
                boss.append(cut)
            if cut.alive:
                cut.run(boss, rolling_cutter, floor_col, mega, shoots)
            else:
                if ending_timer == 1:
                    pygame.mixer.music.load("./audio/music/Victory_theme.mp3")
                    pygame.mixer.music.play()

                GAME.src.global_var.stop_time = True
                ending_timer += 1
            if len(rolling_cutter) == 1:
                cut.with_scissors = False
                rolling_cutter[0].run(cut, rolling_cutter, mega)
            else:
                cut.with_scissors = True

        mega.run()
        if not mega.mid_transition:
            stage.spawn(segment, enemies_bl, "blaster")
            stage.spawn(segment, enemies_oct_b, "octopus")
            stage.spawn(segment, enemies_b_e, "big_eye")
            buster.run(shoots, mega)
            blaster.run(enemies_bl, bullets, shoots, mega)
            octopus_bat.run(enemies_oct_b, floor_col, shoots, octopus_timer, mega)
            eye.run(enemies_b_e, floor_col, shoots, mega)
            mega.display_health()
            doors = stage.list_doors(segment)
            for door in doors:
                door.run(mega)
        bundy.run(random_enemies, shoots, mega)
        mega.display_health()
        if mega.mid_transition:
            random_enemies = []

        camera.cam_move(
            segment,
            [mega.x, mega.y],
            mega.speed,
            mega.left,
        )

        if mega.y - GAME.src.global_var.camera_y > 1080:
            mega.health = 0

        pygame.display.flip()

        dt = clock.tick(55) / 1000
        timer -= dt
        octopus_timer -= dt
        if octopus_timer <= 0:
            octopus_timer = 2

        if not GAME.src.global_var.disable_bunby_spawn:
            if timer <= 0:
                random_enemies = bundy.respawn_bunby(segment, random_enemies)
                timer = 3
        if mega.x >= 9622:
            GAME.src.global_var.enable_boss = True

        if ending_timer == 360:
            running = False
    if not cut.alive:
        ending_screen(screen)

    quit()


main()
