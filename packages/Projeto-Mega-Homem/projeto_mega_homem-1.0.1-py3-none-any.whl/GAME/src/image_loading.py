import pygame
import os


def image_loader(sprite_directory):
    sprites = {}

    for image in os.listdir(sprite_directory):
        try:
            sprites[image.split(".")[0]] = pygame.image.load(
                "{}/{}".format(sprite_directory, image)
            )
        except pygame.error:
            pass
    return sprites
