class Settings:
    """A class to stote all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings:
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)
        # Ship settings
        self.ship_speed = 3
        self.ship_limit = 3
        # Bullet settings:
        self.bullet_speed = 5.0
        self.bullet_width = 10
        self.bullet_height = 10
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 100
        # Alien settings
        self.alien_speed = 0.5
        self.fleet_drop_speed = 5
        # fleet direction of 1 represents right, -1 represents left
        self.fleet_direction = 1