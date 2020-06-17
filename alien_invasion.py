import sys 

import pygame

def run_game():
    #creating screen object
    pygame.init()
    screen = pygame.display.set_mode((1400, 900))
    pygame.display.set_caption("Alien Invasion")

    #background color
    bg_color = (204, 204, 204)

    #main loop of the game
    while True:

        #keyboard&mouse
        for event in pygame.event.get():
            screen.fill(bg_color)
            #make screen visible
            # pygame.display.flip()
            if event.type == pygame.QUIT:
                sys.exit()
        
        pygame.display.flip()

    
    
run_game()


