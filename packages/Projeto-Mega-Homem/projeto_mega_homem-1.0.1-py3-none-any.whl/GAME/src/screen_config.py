import pygame


class Screen:
    resolution = (720, 720)
    display_screen = pygame.display.set_mode(resolution)

    def screen_to_blit(self):
        return self.display_screen
