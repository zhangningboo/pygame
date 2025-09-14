from pathlib import Path
import pygame

size = width, height = 600, 600

pygame.init()
screen = pygame.display.set_mode(size, flags=pygame.RESIZABLE, depth=32)
pygame.display.set_caption("测试颜色值透明度")

curr_path = Path(__file__).parent
image = pygame.image.load(curr_path.joinpath('colorkeys.png'))
image.set_colorkey((255, 0, 0))  # 红色透明
# image.set_colorkey((0, 255, 0))  # 红色透明  最后一个set_colorkey生效

# image = pygame.image.load(curr_path.joinpath('not_alpha.png'))
# image.set_colorkey((255, 255, 255))

image.set_alpha(127)  # 设置整体透明度，0-完全透明，255-不透明

while True:
    screen.fill((25, 102, 173))
    screen.blit(image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            exit(0)
    pygame.display.update()