# In windows, use py instead of python3(wsl) to run the game
import sys

from settings import Settings
from ship import Ship
import game_functions as gf

import pygame

def run_game():
    # Initialize Pygame and create a window
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) # a surface element, every time the screen is updated in a loop, it is redrawn
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings, screen)

    # main loop of the game
    while True:

        gf.check_events(ship)
        gf.update_screen(ai_settings, screen, ship)

run_game()