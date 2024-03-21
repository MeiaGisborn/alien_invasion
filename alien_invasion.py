import sys
from settings import Settings
import pygame
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, create resources"""
        pygame.init()
        # Clock to control the frame rate of a game
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        

    
    def run_game(self):
        """Start the main loop of the game"""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)


    def _check_events(self):
        # Watch keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


    def _update_screen(self):
        """update images on the screen and flip it to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Make the most recently drawn screen visible
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()