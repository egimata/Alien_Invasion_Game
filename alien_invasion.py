import sys 

import pygame

def run_game():
    #creating screen object
    pygame.init()
    screen = pygame.display.set_mode((1400, 900))
    pygame.display.set_caption("Alien Invasion")

    #main loop of the game
    while True:

        #keyboard&mouse
        for event in pygame.event.get():
            if event.type == pygame.quit():
                sys.exit()
        
        pygame.display.flip()

run_game()