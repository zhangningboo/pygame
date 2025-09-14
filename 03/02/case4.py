import optparse
import pygame

Usage = "图片透明格式转换"
Parser = optparse.OptionParser(usage=Usage)


def main(args):
    pygame.init()

    size = 1, 1
    pygame.display.set_mode(size=size)
    image_sur = pygame.image.load(args[0]).convert_alpha()

    pixel = pygame.PixelArray(image_sur)
    pixel.replace((255, 255, 255, 255), (255, 255, 255, 0))  # 白色完全透明
    sur = pixel.make_surface()
    pixel.close()
    pygame.image.save(sur, args[1])
    pygame.quit()


if __name__ == '__main__':
    options, args = Parser.parse_args()
    if len(args) != 2:
        Parser.print_help()
        exit(1)
    main(args)