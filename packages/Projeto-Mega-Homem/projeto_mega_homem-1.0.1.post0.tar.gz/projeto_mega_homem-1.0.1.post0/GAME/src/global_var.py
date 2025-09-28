from pathlib import Path
from GAME.src.image_loading import image_loader

path = str(Path(__file__).parent)

tittle_screen_spr = image_loader(path + "/sprites/Tittle_Screen")
ending_screen_spr = image_loader(path + "/sprites/Ending_Screen")

megaman_sprites = image_loader(path + "/sprites/Megaman_Sprites")

helicopter_sprites = image_loader(
    path + "/sprites/Enemy_Sprites/Helicopter_Helicopter_Sprites"
)

blaster_sprites = image_loader(path + "/sprites/Enemy_Sprites/Blaster_Sprites")

octopus_sprites = image_loader(path + "/sprites/Enemy_Sprites/Octopus_Sprites")

bigeye_sprites = image_loader(path + "/sprites/Enemy_Sprites/Big_Eye_Sprites")

stage_sprites = image_loader(path + "/sprites/Stage")

pj_sprites = image_loader(path + "/sprites/Enemy_Sprites/Projectiles_Sprites")

cutman_sprites = image_loader(path + "/sprites/Boss_Sprites")
debug_mode = False

camera_x = 0
camera_y = 0

shoots = 0

disable_bunby_spawn = False

stop_time = False
first_door_open = False
second_door_open = False
enable_boss = False

checkpoint = False
