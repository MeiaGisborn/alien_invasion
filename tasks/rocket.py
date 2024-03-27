# 12-4. Rocket: Make a game that begins with a rocket in the center of the
# screen. Allow the player to move the rocket up, down, left, or right using the
# four arrow keys. Make sure the rocket never moves beyond any edge of the
# screen.

import pygame
import sys

class RocketSettings:
    
    def __init__(self):
        self.screen_width = 1200 
        self.screen_height = 800
        self.background_color = (255, 255, 255)
        self.rocket_speed = 1.5
        
class Rocket:
    
    def __init__(self, rk):
        self.screen = rk.screen
        self.settings = rk.settings
        self.screen_rect = rk.screen.get_rect()
        self.image = pygame.image.load('assets/rocket.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.rocket_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed
        self.rect.x = self.x
        self.rect.y = self.y
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        
        
class RocketGame:
    
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = RocketSettings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Rocket game")
        self.rocket = Rocket(self)
        
    def run_game(self):
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()
            self.clock.tick(60)
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_q:
            sys.exit()
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = False
            
    def _update_screen(self):
        self.screen.fill(self.settings.background_color)
        self.rocket.blitme()
        pygame.display.flip()
        
if __name__ == '__main__':
    rk = RocketGame()
    rk.run_game()