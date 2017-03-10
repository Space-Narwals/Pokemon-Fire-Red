import pygame;
import os
import sprite_manager;


version = "1.0.0 BETA"
SCALE = 3
clock = pygame.time.Clock()
BLACK = (0, 0, 0);

def main():
    running = True

    #Print debug and setup screen.
    print "Starting Pokemon Fire Red Version:", version
    pygame.init()
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.display.set_caption("Pokemon Fire Red " + version)
    screen = pygame.display.set_mode((240 * SCALE, 160 * SCALE))

    #Setup background stuff.
    background = sprite_manager.PalletTownSpawnSprite(screen);
    background_group = pygame.sprite.RenderPlain(background);

    #Initilize game loop.
    while running:
        clock.tick(60);
        screen.fill(BLACK)
        background.update();
        background_group.draw(screen);
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                print(event)

        keys = pygame.key.get_pressed();
        if keys[pygame.K_UP]:
            background.move_block("up");
        if keys[pygame.K_DOWN]:
            background.move_block("down");
        if keys[pygame.K_RIGHT]:
            background.move_block("right");
        if keys[pygame.K_LEFT]:
            background.move_block("left");
    quit()

if __name__ == "__main__": main()