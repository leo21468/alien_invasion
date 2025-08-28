# divide the game functions part in the main function to apart it from functions like updating the scren
import sys

import pygame

def check_keydown_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship):
    # monitor events from the keyboard and mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # click the close window button or key press
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship):
    # update the screen with the latest game elements
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()