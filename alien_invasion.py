# In windows, use py instead of python3(wsl) to run the game
import sys

from settings import Settings

import pygame

def run_game():
    # Initialize Pygame and create a window
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) # a surface element, every time the screen is updated in a loop, it is redrawn
    pygame.display.set_caption("Alien Invasion")

    # main loop of the game
    while True:

        # monitor events from the keyboard and mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # click the close window button
                sys.exit()
        
        screen.fill(ai_settings.bg_color) # fill the screen with the background color

        # make the most recently drawn surface visible (keep updating)
        pygame.display.flip()

run_game()