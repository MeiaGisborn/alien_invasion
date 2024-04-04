import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""
    
    def __init__(self, ss):
        """Initialize the alien and set it's starting position"""
        super().__init__()
        self.screen = ss.screen
        self.settings = ss.settings
        # Load the alien image and set its rect attr.
        self.image = pygame.image.load('assets/alien.bmp')
        self.rect = self.image.get_rect()
        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)

        
    def check_edges(self):
        """Return true if alien is at the edge of screen"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
        
            
    def update(self):
        """Move the alien to the right or left"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x