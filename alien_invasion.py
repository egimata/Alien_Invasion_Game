import sys 
import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from alien import Alien

def run_game():
    #creating screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #inserting ship
    ship = Ship(ai_settings, screen)
    #bullets in a group
    bullets = Group()
    #adding alien
    alien = Alien(ai_settings, screen)


    #main loop of the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, alien, bullets)


    
    
run_game()


