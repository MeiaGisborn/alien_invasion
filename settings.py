class Settings:
    """A class to stote all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings:
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)
        # Ship settings
        self.ship_speed = 1.5
        # Bullet settings:
        self.bullet_speed = 5.0
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10