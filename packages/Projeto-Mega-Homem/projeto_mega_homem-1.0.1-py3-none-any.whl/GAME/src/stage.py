import pygame
import global_var
import enemy_spawns
from screen_config import Screen
from global_var import stage_sprites
from stage_coll import Stage_collisions


class Stage(Stage_collisions):
    def __init__(self):
        super().__init__()
        self.screen = Screen.display_screen
        self.sprites = [
            stage_sprites["Cutman_Stage_Segment_1"],
            stage_sprites["Cutman_Stage_Segment_2"],
            stage_sprites["Cutman_Stage_Segment_3"],
            stage_sprites["Cutman_Stage_Segment_4"],
            stage_sprites["Cutman_Stage_Segment_5"],
            stage_sprites["Cutman_Stage_Segment_6"],
            stage_sprites["Cutman_Stage_Segment_7"],
            stage_sprites["Cutman_Stage_Segment_8"],
        ]

        self.sprite_pos = {
            "Cutman_Stage_Segment_1": [0, 0],
            "Cutman_Stage_Segment_2": [2304, -3072],
            "Cutman_Stage_Segment_3": [2304, -3072],
            "Cutman_Stage_Segment_4": [1280 * 3, -3072 * 2],
            "Cutman_Stage_Segment_5": [1280 * 3, -3072 * 2],
            "Cutman_Stage_Segment_6": [1280 * 4 + 256, -3072 * 2],
            "Cutman_Stage_Segment_7": [1280 * 4 + 256, -3072 * 2 + 768 * 3],
            "Cutman_Stage_Segment_8": [1280 * 4 + 256 * 4 - 3, -3072 * 2 + 768 * 3],
        }

        self.selected_sprite = "Cutman_Stage_Segment_1"
        self.used_sprite = pygame.transform.scale_by(self.sprites[0], 3)

    def draw_stage(self):
        cx = global_var.camera_x
        cy = global_var.camera_y
        self.screen.blit(
            self.used_sprite,
            (
                self.sprite_pos[self.selected_sprite][0] - cx,
                self.sprite_pos[self.selected_sprite][1] - cy,
            ),
        )

    def handle_coll(self):
        debug = global_var.debug_mode
        self.update_coll()
        for coll in self.floor_collisions:
            if debug:
                pygame.draw.rect(self.screen, "red", coll)
        return self.floor_collisions

    def handle_stair_coll(self):
        debug = global_var.debug_mode
        self.update_stair_coll()
        for coll in self.stairs_collisions:
            if debug:
                pygame.draw.rect(self.screen, "green", coll)
        return self.stairs_collisions

    def handle_death_coll(self):
        debug = global_var.debug_mode
        self.update_death_coll()
        for coll in self.death_collisions:
            if debug:
                pygame.draw.rect(self.screen, "blue", coll)
        return self.death_collisions

    def change_segment(self, coordinates):
        on_seg_1 = coordinates[0] < 2690 and coordinates[1] > -30
        on_seg_2 = coordinates[0] >= 2690 or coordinates[1] < -30
        on_seg_3 = (coordinates[0] >= 2496 and coordinates[1] <= -2490) or coordinates[
            0
        ] > 3200
        on_seg_4 = coordinates[0] >= 4410 or coordinates[1] <= -3120
        on_seg_5 = coordinates[0] >= 4120 and coordinates[1] <= -5560
        on_seg_6 = coordinates[0] >= 5412 and coordinates[1] > -5560
        on_seg_7 = coordinates[0] >= 5412 and coordinates[1] > -3822
        on_seg_8 = coordinates[0] >= 6800

        if on_seg_8:
            self.selected_sprite = "Cutman_Stage_Segment_8"
            self.used_sprite = pygame.transform.scale_by(
                self.sprites[7].convert_alpha(), 3
            )
            self.selected_seg = "Cutman_Stage_Segment_8"
        elif on_seg_7:
            self.selected_sprite = "Cutman_Stage_Segment_7"
            self.used_sprite = pygame.transform.scale_by(
                self.sprites[6].convert_alpha(), 3
            )
            self.selected_seg = "Cutman_Stage_Segment_7"

        elif on_seg_6:
            self.selected_sprite = "Cutman_Stage_Segment_6"
            self.used_sprite = pygame.transform.scale_by(
                self.sprites[5].convert_alpha(), 3
            )
            self.selected_seg = "Cutman_Stage_Segment_6"
        elif on_seg_5:
            self.selected_sprite = "Cutman_Stage_Segment_5"
            self.used_sprite = pygame.transform.scale_by(
                self.sprites[4].convert_alpha(), 3
            )
            self.selected_seg = "Cutman_Stage_Segment_5"
        elif on_seg_4:
            self.selected_sprite = "Cutman_Stage_Segment_4"
            self.used_sprite = pygame.transform.scale_by(
                self.sprites[3].convert_alpha(), 3
            )
            self.selected_seg = "Cutman_Stage_Segment_4"
        elif on_seg_3:
            self.selected_sprite = "Cutman_Stage_Segment_3"
            self.used_sprite = pygame.transform.scale_by(
                self.sprites[2].convert_alpha(), 3
            )
            self.selected_seg = "Cutman_Stage_Segment_3"
        elif on_seg_2:
            self.selected_sprite = "Cutman_Stage_Segment_2"
            self.used_sprite = pygame.transform.scale_by(
                self.sprites[1].convert_alpha(), 3
            )
            self.selected_seg = "Cutman_Stage_Segment_2"
        elif on_seg_1:
            self.selected_sprite = "Cutman_Stage_Segment_1"
            self.used_sprite = pygame.transform.scale_by(
                self.sprites[0].convert_alpha(), 3
            )
            self.selected_seg = "Cutman_Stage_Segment_1"

    def spawn(self, segment, enemies, name):
        if name == "blaster":
            if (
                segment == "Cutman_Stage_Segment_1"
                or segment == "Cutman_Stage_Segment_2"
            ):
                enemy_spawns.spawn_blasters(segment, enemies)
        if name == "octopus":
            if (
                segment == "Cutman_Stage_Segment_3"
                or segment == "Cutman_Stage_Segment_4"
            ):
                enemy_spawns.spawn_octopus(segment, enemies)
        if name == "big_eye":
            if segment == "Cutman_Stage_Segment_7":
                enemy_spawns.spawn_big_eye(segment, enemies)
