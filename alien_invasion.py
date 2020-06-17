import sys 
import pygame
from settings import Settings


def run_game():
    #creating screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #main loop of the game
    while True:

        #keyboard&mouse
        for event in pygame.event.get():

            #fill screen with bg color
            screen.fill(ai_settings.bg_color) 
            if event.type == pygame.QUIT:
                sys.exit()
        #make screen visible
        pygame.display.flip()
    
    
run_game()


