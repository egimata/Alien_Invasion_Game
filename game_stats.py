import sys

class GameStats():
    """Tracks stats for the game/gameplayer"""

    def __init__(self, ai_settings):
        """initializes stats"""
        self.ai_settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        """init stats that can change during game"""
        self.ships_left = self.ai_settings.ship_limit