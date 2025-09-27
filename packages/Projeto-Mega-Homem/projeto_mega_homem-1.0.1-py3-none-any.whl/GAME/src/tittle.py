import pygame
import global_var


ts = global_var.tittle_screen_spr["Tittle_Screen"]
button = global_var.tittle_screen_spr["Tittle_Button"]


def tittle_screen(screen):
    tittle = 1
    timer = 0
    while tittle:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:
                    tittle = False

        timer += 1
        screen.display_screen.blit(pygame.transform.scale_by(ts, 3), (-30, 0))
        if timer < 40:
            screen.display_screen.blit(pygame.transform.scale_by(button, 3), (235, 450))
        pygame.display.flip()
        if timer == 80:
            timer = 0
