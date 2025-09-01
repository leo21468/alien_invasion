# In windows, use py instead of python3(wsl) to run the game
import sys

from settings import Settings
from ship import Ship
from pygame.sprite import Group
import game_functions as gf

import pygame

def run_game():
    # Initialize Pygame and create a window
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) # a surface element, every time the screen is updated in a loop, it is redrawn
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings, screen)
    # create a group saving bullets, it's like a list, but offering more functionality
    bullets = Group() # if we create a group in the loop, it will be too slow

    # main loop of the game
    while True:

        gf.check_events(ai_settings, screen, ship, bullets) # need to give information to bullets
        ship.update() # don't forget to update the ship's position
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()