import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_settings, screen):
        """init alien and set starting position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #load img and set rect attribute
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()

        #start at top left corner of scr
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store position
        self.x = float(self.rect.x)
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)