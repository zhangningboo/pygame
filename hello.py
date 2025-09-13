import pygame
from pygame.locals import QUIT

pygame.init()
# screen = pygame.display.set_mode(size=(500, 200), flags=pygame.RESIZABLE, depth=32)
screen = pygame.display.set_mode(size=(500, 200), flags=pygame.FULLSCREEN, depth=32)

font = pygame.font.SysFont(name=None, size=60)
mingri = font.render('Hello, Pygame World!', True, (255, 255, 255))

import sys

while True:
    screen.fill(color=(25, 102, 173))
    screen.blit(source=mingri, dest=(50, 80))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    pygame.display.update()
