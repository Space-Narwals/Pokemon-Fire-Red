import pygame;


SCALE = 3;
x = 84
y = 96

screen = main.screen;

class PalletTownSprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.image.load('res/img/pallet-town-interior.png')
        self.image = pygame.transform.scale(pygame.image.load('res/img/pallet-town-interior.png'), (176 * SCALE, 144 * SCALE))
        self.rect = self.image.get_rect()
        self.rect.move_ip(screen.get_rect().centerx, screen.get_rect().centery);
