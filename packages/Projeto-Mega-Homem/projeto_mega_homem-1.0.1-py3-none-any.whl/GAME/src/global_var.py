from image_loading import image_loader

tittle_screen_spr = image_loader("./sprites/Tittle_Screen")
ending_screen_spr = image_loader("./sprites/Ending_Screen")

megaman_sprites = image_loader("./sprites/Megaman_Sprites")

helicopter_sprites = image_loader(
    "./sprites/Enemy_Sprites/Helicopter_Helicopter_Sprites"
)

blaster_sprites = image_loader("./sprites/Enemy_Sprites/Blaster_Sprites")

octopus_sprites = image_loader("./sprites/Enemy_Sprites/Octopus_Sprites")

bigeye_sprites = image_loader("./sprites/Enemy_Sprites/Big_Eye_Sprites")

stage_sprites = image_loader("./sprites/Stage")

pj_sprites = image_loader("./sprites/Enemy_Sprites/Projectiles_Sprites")

cutman_sprites = image_loader("./sprites/Boss_Sprites")
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
