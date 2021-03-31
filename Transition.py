import pygame
from State import *
pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
class Transition():
    def __init__(self, startState_, endState_, pos_):
        self.acceptingSymbol = ""
        self.startState = startState_
        self.endState = endState_
        self.pos = self.calcPos(pos_)

    def calcPos(self, pos_):
        #Do some maths here to make the arrows line up better
        if self.startState != self.endState:
            pass
        return pos_
