import pygame;

SCALE = 3;

class PalletTownSpawnSprite(pygame.sprite.Sprite):
    x = 0
    y = 0
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load('res/img/pallet-town-interior.png'), (176 * SCALE, 144 * SCALE))
        self.rect = self.image.get_rect()
        self.rect.move_ip(screen.get_rect().centerx - self.rect.centerx, screen.get_rect().centery - self.rect.centery);
    def move_block(self, direction):
        changeX = 0;
        changeY = 0;
        if direction == "up":
            changeY = -4;
        elif direction == "down":
            changeY = 4;
        elif direction == "right":
            changeX = 4;
        elif direction == "left":
            changeX = -4;

        self.rect.move_ip(changeX, changeY);
