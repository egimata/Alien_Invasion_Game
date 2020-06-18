import pygame

class Ship():

    def __init__(self, screen):
        """initialize the ship and set its position"""
        self.screen = screen

        #loading img
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #start each ship at the bottom center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #movement
        self.moving_right = False
    
    def update(self):
        """update the ship's position based on movement flag"""
        if self.moving_right:
            self.rect.centerx += 1

    def blitme(self):
        """draw ship at current location"""
        self.screen.blit(self.image, self.rect)