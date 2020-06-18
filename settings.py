class Settings():
    """A class to store all settings for the game"""

    def __init__(self):
        #screen settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (204, 204, 204)
        #ship speed
        self.ship_speed_factor = 1.5

        self.bullet_speed_factor = 1
        self.bullet_width = 4
        self.bullet_height = 18
        self.bullet_color = (255, 51, 51)
        self.bullets_allowed = 5

        