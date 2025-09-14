import math
import sys
from pathlib import Path
from functools import lru_cache

import pygame
from pygame.locals import *


SIZE = WIDTH, HEIGHT = 640, 600
FPS = 60
BG_COLOR = pygame.Color('white')
BLACK = pygame.Color('black')
WHITE = pygame.Color('white')
FONT_BG_COLOR = (183, 23, 27, 100)


@lru_cache(maxsize=360 * 6)
def cul_posi(angle, posi, radius):
    """计算圆心坐标"""
    dox_x = round(posi[0] + radius * math.cos(math.radians(angle)))
    dox_y = round(posi[1] + radius * math.sin(math.radians(angle)))
    return dox_x, dox_y


pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("太极")
clock = pygame.time.Clock()

root_path = Path(__file__).parent.parent.parent
font = pygame.font.Font(root_path.joinpath('华文楷体.TTF'), size=50)

radius = 160
angle = 90

posi = (WIDTH // 2 - 60, HEIGHT // 2)
font.set_bold(True)

font_01 = font.render('太', True, WHITE, FONT_BG_COLOR)
font_02 = font.render('极', True, WHITE, FONT_BG_COLOR)
font_03 = font.render('图', True, WHITE, FONT_BG_COLOR)

font_rect = font_01.get_rect()
font_linesize = font.get_linesize()
print(f"字体尺寸：{font_rect.size}, 行高：{font_linesize}")

title_posi = (500, 40)

while True:
    screen.fill(BG_COLOR)
    # 实心园
    pygame.draw.circle(screen, BLACK, posi, radius)
    dot_x1, dot_y1 = cul_posi(angle=angle, posi=posi, radius=radius)
    dot_x4, dot_y4 = cul_posi(angle=angle + 180, posi=posi, radius=radius)
    dot_x2, dot_y2 = cul_posi(angle=angle + 90, posi=(dot_x1, dot_y1), radius=radius)
    dot_x3, dot_y3 = cul_posi(angle=angle + 90, posi=(dot_x4, dot_y4), radius=radius)
    # 长方形
    pygame.draw.polygon(screen, BG_COLOR, [(dot_x1, dot_y1), (dot_x2, dot_y2), (dot_x3, dot_y3), (dot_x4, dot_y4)])
    # 小圆
    posi_x1, posi_y1 = cul_posi(angle=angle, posi=posi, radius=radius // 2)
    posi_x2, posi_y2 = cul_posi(angle=angle, posi=(dot_x4, dot_y4), radius=radius // 2)
    # 填充小圆
    pygame.draw.circle(screen, BLACK, (posi_x1, posi_y1), radius // 2)
    pygame.draw.circle(screen, WHITE, (posi_x2, posi_y2), radius // 2)
    # 小圆内小圆
    pygame.draw.circle(screen, WHITE, (posi_x1, posi_y1), radius // 10)
    pygame.draw.circle(screen, BLACK, (posi_x2, posi_y2), radius // 10)

    angle += 1
    if angle == 361:
        angle = 0

    pygame.draw.rect(screen, FONT_BG_COLOR, (title_posi[0] - 8, title_posi[1] - 18, font_rect.width + 16, 16 + 100 * 3))

    screen.blit(font_01, title_posi)
    screen.blit(font_02, (title_posi[0], title_posi[1] + 100))
    screen.blit(font_03, (title_posi[0], title_posi[1] + 100 * 2))

    # 圆形边框
    pygame.draw.circle(screen, BLACK, posi, radius, 1)

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit(0)

    pygame.display.update()
    clock.tick(FPS)