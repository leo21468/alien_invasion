import pygame

class Ship():
    
    def __init__(self, screen):
        self.screen = screen

        # load the image of the ship and get its outer rectangle
        self.image = pygame.image.load(r'images\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # put the ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx # center, centerx, centery
        self.rect.bottom = self.screen_rect.bottom # top, bottom, left, right

    def blitme(self):
        # draw the ship at its current location
        self.screen.blit(self.image, self.rect)