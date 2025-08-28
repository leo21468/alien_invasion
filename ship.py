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

        # the moving flag to control the ship's movement smoothly
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # update the ship's position based on the movement flags
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 1
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= 1

    def blitme(self):
        # draw the ship at its current location
        self.screen.blit(self.image, self.rect)