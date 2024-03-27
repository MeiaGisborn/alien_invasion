# 12-5. Keys: Make a Pygame file that creates an empty screen. In the event
# loop, print the event.key attribute whenever a pygame.KEYDOWN event is
# detected. Run the program and press various keys to see how Pygame
# responds.

import pygame
import sys

class EventKeyPrint:
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("Event Key Print")
        
    def run_app(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    print(pygame.key.name(event.key))
            pygame.display.flip()
            

if __name__ == '__main__':
    ekp = EventKeyPrint()
    ekp.run_app()