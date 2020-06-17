import sys
import pygame

def check_events():
    """keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    """updates images on screen"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()