import pygame
import global_var

es = global_var.ending_screen_spr["Ending_Screen"]


def ending_screen(screen):
    pygame.mixer.music.stop()
    pygame.mixer.music.load("./audio/music/Ending_theme.mp3")
    pygame.mixer.music.play(-1)
    ending = 1
    while ending:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                ending = False

        screen.display_screen.blit(pygame.transform.scale_by(es, 3), (-24, 0))

        pygame.display.flip()
