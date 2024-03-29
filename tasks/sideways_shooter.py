# 12-6. Sideways Shooter: Write a game that places a ship on the left side
# of the screen and allows the player to move the ship up and down. Make the
# ship fire a bullet that travels right across the screen when the player presses
# the spacebar. Make sure bullets are deleted once they disappear off the
# screen.

import pygame
from pygame.sprite import Sprite
import sys

class SidewaysSettings:
    
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.background_color = (255, 255, 255)
        self.rocket_speed = 1.5
        # Bullet settings
        self.bullet_speed = 5.0
        self.bullet_width = 8
        self.bullet_height = 3
        self.bullet_color = (0, 0, 0)
        self.bullets_allowed = 10
        
        
class SidewaysRocket:
    
    def __init__(self, ss):
        self.screen = ss.screen
        self.settings = ss.settings
        self.screen_rect = ss.screen.get_rect()
        self.image = pygame.image.load('assets/rocket1.jpg')
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft
        #self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.moving_up = False
        self.moving_down = False
        
    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed
        # self.rect.x = self.x
        self.rect.y = self.y
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Bullet(Sprite):
    
    def __init__(self, ss):
        super().__init__()
        self.screen = ss.screen
        self.settings = ss.settings
        self.color = self.settings.bullet_color
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, 
                                self.settings.bullet_height)
        self.rect.midleft = ss.rocket.rect.midleft
        self.x = float(self.rect.x)
        
    def update(self):
        self.x += self.settings.bullet_speed
        self.rect.x = self.x
        
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        
    
class SidewaysShooter:
    
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = SidewaysSettings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Sideway Shooter")
        self.rocket = SidewaysRocket(self)
        self.bullets = pygame.sprite.Group()
        

    def run_game(self):
        while True:
            self._check_events()
            self.rocket.update()
            self._update_bullets()
            print(len(self.bullets))
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
        if event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            
    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False
            
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            
    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.settings.screen_width:
                self.bullets.remove(bullet)
    
    def _update_screen(self):
        self.screen.fill(self.settings.background_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.rocket.blitme()
        pygame.display.flip()
            
            
            
if __name__ == '__main__':
    ss = SidewaysShooter()
    ss.run_game()
                