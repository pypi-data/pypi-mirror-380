import pygame
from screen_config import Screen


class Life_bar(Screen):
    def __init__(self, hp, character):
        self.health = hp
        self.character = character

    def display_health(self):
        if self.character == "megaman":
            pygame.draw.rect(
                self.display_screen,
                "black",
                (80, 23, 24, 168),
            )
            for i in range(self.health):
                pygame.draw.rect(
                    self.display_screen, "#F0DC9D", (83, 185 - 6 * i, 18, 3)
                )
                pygame.draw.rect(
                    self.display_screen, "#F1F3F5", (89, 185 - 6 * i, 6, 3)
                )
        else:
            pygame.draw.rect(
                self.display_screen,
                "black",
                (120, 23, 24, 168),
            )
            for i in range(self.health):
                pygame.draw.rect(
                    self.display_screen, "#DD0458", (123, 185 - 6 * i, 18, 3)
                )
                pygame.draw.rect(
                    self.display_screen, "#F39439", (129, 185 - 6 * i, 6, 3)
                )
