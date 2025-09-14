from pathlib import Path

import pygame

pygame.init()


colors = pygame.Surface(size=(4090, 4096), depth=32)
for r in range(256):
    x = (r % 16) * 256
    y = (r // 16) * 256
    for g in range(256):
        for b in range(256):
            colors.set_at((x + g, y + b), (r, g, b))
pygame.image.save(colors, Path(__file__).parent.joinpath("colors.png"))
pygame.quit()