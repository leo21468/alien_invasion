class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's screen settings."""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 192, 203) # light pink
        self.ship_speed_factor = 1.5 # set the speed of the ship