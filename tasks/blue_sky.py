import pygame
import sys

class BlueSky():
    """Overall class to show the empty blue screen"""
    def __init__(self):
        """Initialize the game and create resources"""
        pygame.init()
        self.screen = pygame.display.set_mode((200, 200))
        self.back_color = (0, 0, 230)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.back_color)
            pygame.display.flip()


if __name__ == '__main__':
    blue_sky_game = BlueSky()
    blue_sky_game.run_game()