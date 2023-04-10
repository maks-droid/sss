import pygame, controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores



def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("КС")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    controls.create_army(screen, inos)
    stats = Stats()
    sc = Scores(screen, stats)
    font = pygame.font.SysFont(None, 80)


    while True:
        controls.events(screen, gun, bullets)
        if stats.run_game == False:
            screen.fill((0, 0, 0))
            play = font.render('Play', True, (255, 0, 0))
            play_rect = play.get_rect()
            screen_rect = screen.get_rect()
            play_rect.center = screen_rect.center

            mouse_pressed = pygame.mouse.get_pressed()
            mouse_pos = pygame.mouse.get_pos()

            screen.blit(play, play_rect)
            if mouse_pressed[0] and play_rect.collidepoint(mouse_pos):
                stats.run_game = True

        if stats.run_game:
            gun.update_gun()
            controls.update(bg_color, screen, stats, sc, gun, inos, bullets)
            controls.update_bullets(screen, stats, sc, inos, bullets)
            controls.update_inos(stats, screen, sc, gun, inos, bullets)
        pygame.display.flip()

run()