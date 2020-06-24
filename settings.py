class Settings():
    """A class to store all settings for the game"""

    def __init__(self):
        #screen settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (204, 204, 204)
        #ship speed
        self.ship_speed_factor = 1
        self.ship_limit = 3

        self.bullet_speed_factor = 3
        self.bullet_width = 300
        self.bullet_height = 60
        self.bullet_color = (255, 51, 51)
        self.bullets_allowed = 7
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 5
        # 1 = right ; -1 = left
        self.fleet_direction = 1
        #game speed on lvlup
        self.speedup_scale = 1.3
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """init settg that change throughout the game"""
        self.ship_speed_factor = 1
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        
        