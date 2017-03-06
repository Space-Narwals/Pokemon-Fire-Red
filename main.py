import pygame;
import os

from sprite.pallettowninterior import PalletTownSprite

version = "1.0.0 BETA"
SCALE = 5
clock = pygame.time.Clock()
GREEN = (124,252,0);


def main():
    print "Starting Pokemon Fire Red Version:", version
    pygame.init()
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.display.set_caption("Pokemon Fire Red " + version)

    screen = pygame.display.set_mode((240 * SCALE, 160 * SCALE))

    terrian_sprites = pygame.sprite.Group();

    while 1:
        clock.tick(60)
        screen.fill(GREEN)
        pygame.display.flip()
main()

