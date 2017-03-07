import pygame;
import os

from sprite.pallettowninterior import PalletTownSprite


version = "1.0.0 BETA"
SCALE = 3
clock = pygame.time.Clock()
GREEN = (124,252,0);
screen = None

def main():
    running = True
    print "Starting Pokemon Fire Red Version:", version
    pygame.init()
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.display.set_caption("Pokemon Fire Red " + version)

    screen = pygame.display.set_mode((240 * SCALE, 160 * SCALE))

    rect = screen.get_rect()
    background = PalletTownSprite();
    background_group = pygame.sprite.RenderPlain(background);

    while running:
        clock.tick(60)
        screen.fill(GREEN)
        background_group.draw(screen);
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                print(event)

    pygame.quit()
    quit()
main()
