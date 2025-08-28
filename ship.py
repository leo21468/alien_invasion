import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        # load the image of the ship and get its outer rectangle
        self.image = pygame.image.load(r'images\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # put the ship at the bottom center of the screen
        self.center = float(self.screen_rect.centerx) # center, centerx, centery (centerx is integer, so we create center_
        self.rect.bottom = self.screen_rect.bottom # top, bottom, left, right

        # the moving flag to control the ship's movement smoothly
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # update the ship's position based on the movement flags
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # update the rect object from self.center (turn float into int)
        self.rect.centerx = self.center

    def blitme(self):
        # draw the ship at its current location
        self.screen.blit(self.image, self.rect)