import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, screen, health=100):
        """initialize the ship and set its position"""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.health = health
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0


        #loading img
        self.image = pygame.transform.scale(pygame.image.load('images/ship.png'), (100, 80))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #start each ship at the bottom center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #decimal value for x and y center.
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # #decimal value for ship's center
        # self.center = float(self.rect.centerx)

        #movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def center_ship(self):
        self.centerx = self.screen_rect.centerx
        self.centery = self.screen_rect.centery
    
    def update(self):
        """update the ship's position based on movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor
        #update rect from self.center - changed for movement in two directions
        if self.moving_left or self.moving_right:
            self.rect.centerx = self.centerx
        if self.moving_up or self.moving_down:
            self.rect.centery = self.centery

    def blitme(self):
        """draw ship at current location"""
        self.screen.blit(self.image, self.rect)