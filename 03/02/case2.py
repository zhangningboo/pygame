from pathlib import Path

import pygame
pygame.init()

success_module_cnt, failure_module_cnt = pygame.init()
print(f"初始化成功模块数：{success_module_cnt}, 失败模块数：{failure_module_cnt}")
if failure_module_cnt > 0:
    print("警告：部分模块初始化失败，请检查环境配置！")
    pygame.quit()
    exit(1)

pygame.display.set_caption("颜色透明度")

curr_path = Path(__file__).parent
root_path = Path(__file__).parent.parent.parent
font = pygame.font.Font(root_path.joinpath('华文楷体.TTF'), size=50)

text = font.render('透明度渐变效果', True, (255, 255, 255))

image = pygame.image.load(curr_path.joinpath('alpha.png'))
# image = pygame.image.load(curr_path.joinpath('not_alpha.png'))
print(f"图片尺寸：{image.get_size()}, 图片格式：{image.get_bitsize()}位")
width, height = image.get_size()
screen = pygame.display.set_mode(size=(width * 2, height * 2), depth=32)
image = image.convert_alpha()

size = 25
while True:
    screen.blit(text, (100, 100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            exit(0)

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            print(f"Mouse clicked at: {x}, {y}")

            screen.blit(image, (x - size, y - size))
    pygame.display.update()