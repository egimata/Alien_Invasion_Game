import sys 
import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard



def main():
    #creating screen object
    pygame.init()
    # FPS = 60
    # clock = pygame.time.Clock()
    
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    def redraw_window():
        screen.blit(ai_settings.bg, (0,0))
        pygame.display.update()
    #play button
    play_button = Button(ai_settings, screen, "Play")

    #inserting ship
    ship = Ship(ai_settings, screen)
    #bullets in a group
    bullets = Group()
    aliens = Group()
    #adding alien
    # alien = Alien(ai_settings, screen)

    #create fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)
    #game stats
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen, stats)



    #main loop of the game
    while True:
        # clock.tick(FPS)
        redraw_window()
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


    
    
main()


