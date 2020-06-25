import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """initialize the ship and set its position"""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #loading img
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #start each ship at the bottom center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #decimal value for ship's center
        self.center = float(self.rect.centerx)

        #movement flags
        self.moving_right = False
        self.moving_left = False

    def center_ship(self):
        self.center = self.screen_rect.centerx
    
    def update(self):
        """update the ship's position based on movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        #update rect from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """draw ship at current location"""
        self.screen.blit(self.image, self.rect)