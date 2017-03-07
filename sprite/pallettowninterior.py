import pygame;
SCALE = 3;

class PalletTownSprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.image.load('res/img/pallet-town-interior.png')
        self.image = pygame.transform.scale(pygame.image.load('res/img/pallet-town-interior.png'), (240 * SCALE, 160 * SCALE))
        self.rect = self.image.get_rect()
