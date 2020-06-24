import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """keypresses and mouse events"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    #adding button to fire bullets
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_ESCAPE:
        sys.exit()

def fire_bullet(ai_settings, screen, ship, bullets):
    """fires bullet without reaching limit"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
    

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets):
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """start new game when clicking play"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        ai_settings.initialize_dynamic_settings()
        #make crusor invis
        pygame.mouse.set_visible(False)
        #resets game stats
        stats.reset_stats()
        stats.game_active = True
        #empties list of aliens and bullets
        aliens.empty()
        bullets.empty()

        #creates new fleet and centers the ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """updates images on screen"""
    screen.fill(ai_settings.bg_color)
    #redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()
    #make the most recently drawn scrn visible
    pygame.display.flip()

def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """updating position of bullets and getting rid of old bullets"""
    bullets.update()
    #gets rid of bullets that disappear
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """responds to bullet-alien collision"""
    #checks for bullets that hits aliens and
    #remove them both
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        stats.score +=ai_settings.alien_points
        sb.prep_score()
    if len(aliens) == 0:
        #destroy existing alien and create new one in the row
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)


def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    """determining the nr of rows to fit aliens in the scr"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """creating alien and place in a row"""
    #space between each alien is = 1 alien width
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number        
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    """creating full fleet of aliens"""
    #creating alien and find nr of aliens in a row
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    
    #create the fleet
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def check_fleet_edges(ai_settings, aliens):
    """responds appropriately if aliens reached the edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """dropping fleet"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """responds to ship being hit"""
    if stats.ships_left > 0:
        #ships_left
        stats.ships_left -= 1
        #emptying list of alien and ship
        aliens.empty()
        bullets.empty()
        #center the ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        #pause
        sleep(0.07)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """check if aliens reached the bottom of the screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #same as ship hit
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """checking if fleet is at an edge"""
    check_fleet_edges(ai_settings, aliens)
    """update pos of all aliens"""
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)



        

