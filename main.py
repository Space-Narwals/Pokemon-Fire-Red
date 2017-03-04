import pygame;
import os

from sprite.pallettowninterior import PalletTownSprite

version = "1.0.0 BETA"
SCALE = 5

def main():
    print "Starting Pokemon Fire Red Version:", version
    pygame.init()
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    try:
        screen = pygame.display.set_mode((240 * SCALE, 160 * SCALE))
        while True:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                break
    finally:
        pygame.quit()
main()

