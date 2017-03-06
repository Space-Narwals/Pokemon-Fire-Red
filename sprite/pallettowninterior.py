import pygame;

class PalletTownSprite(pygame.sprite.Sprite):

    def __init__(self, id):
        super.__init__();
        if id == 1:
            print "Selecting 1"