import pygame
pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
class State():
    def __init__(self, pos_, accepting_):
        self.pos = pos_
        self.accepting = accepting_
        self.name = ""

    def show(self, surface, stateSize):
        pygame.draw.circle(surface, BLACK, self.pos, stateSize, 1)
        if self.accepting:
            pygame.draw.circle(surface, BLACK, self.pos, stateSize * 0.84, 1)
