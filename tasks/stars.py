# 13-1. Stars: Find an image of a star. Make a grid of stars appear on the
# screen.
import sys
import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    
    def __init__(self, sg):
        super().__init__()
        self.screen = sg.screen
        self.image = pygame.image.load('assets/star.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        
        
class Settings:
    
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (255, 255, 255)
        
class StarGame:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.bg_color = self.settings.bg_color
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Sea of Stars")
        self.stars = pygame.sprite.Group()
        self._create_sea()
        
        
    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
    def _create_star(self, x_position, y_position):
        new_star = Star(self)
        new_star.x = x_position
        new_star.rect.x = x_position
        new_star.rect.y = y_position
        self.stars.add(new_star)
    
    def _create_sea(self):
        star = Star(self)
        star_width, star_height = star.rect.size
        current_x, current_y = star_width, star_height
        while current_y < (self.settings.screen_height - 3 * star_height):
            while current_x < (self.settings.screen_width - 2 * star_width):
                self._create_star(current_x, current_y)
                current_x += 2 * star_width   
            current_x = star_height
            current_y += 2 * star_height
            
            
    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.stars.draw(self.screen)
        pygame.display.flip()
        
if __name__ == '__main__':
    sg = StarGame()
    sg.run_game()
    sg._create_sea()    