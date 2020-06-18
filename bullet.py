import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """managing bullets that come from the ship"""

    def __init__(self, ai_settings, screen, ship)
    """creating bullet object at ship's position"""
    super(Bullet, self).__init__()
    self.screen = screen

    """create bullet rect at (0, 0)"""
    self.rect = pygame.Rect(0,0, ai_settings.bullet_width, ai_settings.bullet_height)
    self.rect.centerx = ship.rect.centerx
    self.y = float(self.rect.y)

    self.color = ai_settings.bullet_color
    self.speed_factor = ai_settings.bullet_speed_factor
    
    def update(self):
        """move bullet up the screen"""
        self.y -= self.speed_factor
        self.rect.y = self.y
    def draw_bullet(self):
        """draw bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)