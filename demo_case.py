import sys
import pygame
from pygame.locals import *

SIZE = WIDTH, HEIGHT = 800, 600
FPS = 60
TITLE = "Mini Pygame Template"
BG_COLOR = (25, 102, 173)

success_module_cnt, failure_module_cnt = pygame.init()
print(f"初始化成功模块数：{success_module_cnt}, 失败模块数：{failure_module_cnt}")
if failure_module_cnt > 0:
    print("警告：部分模块初始化失败，请检查环境配置！")
    sys.exit(1)

pygame.mixer.init()  # 初始化音频模块

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

font = pygame.font.Font('./华文楷体.TTF', size=60)

fonts = pygame.font.get_fonts()
fonts.sort()
print(f"系统可用字体列表：{fonts}")

game_name = font.render(u'拼图游戏', True, (255, 255, 255))
button_names = font.render(u'开始    退出', True, (255, 255, 255))

running = True
while running:
    screen.fill(BG_COLOR)
    screen.blit(source=game_name, dest=(WIDTH // 2 - 100, HEIGHT // 4))
    screen.blit(source=button_names, dest=(WIDTH // 2 - 100, HEIGHT // 2))

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
    if not running:
        break
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit(0)