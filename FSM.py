import pygame, random, sys, math, time
from pygame.locals import *
from pygame.event import *
from pygame.display import *
from State import *
from Transition import *
pygame.init()

surface = set_mode((600, 600))
set_caption("Finite State Machine")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

stateSize = 30

states = [] #List of state objects
transitions = {} #List of transitions linked by state name

activeTransition = []
drawActiveTransition = False

def drawFSM():
    for i in range(len(states)):
        states[i].show(surface, stateSize)
        if states[i] in transitions:
            for j in range(len(transitions[states[i]])):
                drawTransition(transitions[states[i]][j].pos)
    if len(activeTransition) != 0:
        drawTransition(activeTransition)
    
        #pygame.draw.line(surface, BLACK, activeTransition[0], activeTransition[1])

def drawTransition(transition):
    start, end = transition[0], transition[1]
    pygame.draw.line(surface, BLACK, start, end)
    rotation = math.degrees(math.atan2(start[1]-end[1], end[0]-start[0]))+90
    pygame.draw.polygon(surface, BLACK, ((end[0]+10*math.sin(math.radians(rotation)), end[1]+10*math.cos(math.radians(rotation))), (end[0]+10*math.sin(math.radians(rotation-120)), end[1]+10*math.cos(math.radians(rotation-120))), (end[0]+10*math.sin(math.radians(rotation+120)), end[1]+10*math.cos(math.radians(rotation+120)))), 1)
    
def addRemoveState(e):
    collision = False
    collidingState = 0
    for i in range(len(states)):
        temp = pygame.Rect(states[i].pos[0] - stateSize / 2, states[i].pos[1] - stateSize / 2, stateSize, stateSize)
        mouse = pygame.Rect(e.pos[0], e.pos[1], 2, 2)
        if temp.colliderect(mouse):
            collision = True
            collidingState = i
    if collision:
        for i in range(len(states)):
            if states[i] in transitions:
                size = len(transitions[states[i]])
                for j in range(size - 1, -1, -1):
                    if states[collidingState] == transitions[states[i]][j].endState:
                        del(transitions[states[i]][j])
        if states[collidingState] in transitions:
            del(transitions[states[collidingState]])
        del(states[collidingState])
    else:
        states.append(State([e.pos[0], e.pos[1]], False))

def toggleAccepting(e):
    for state in states:
        temp = pygame.Rect(state.pos[0] - stateSize / 2, state.pos[1] - stateSize / 2, stateSize, stateSize)
        mouse = pygame.Rect(e.pos[0], e.pos[1], 2, 2)
        if temp.colliderect(mouse):
            state.accepting = not state.accepting

def addTransition():
    collisionStart = False
    collidingStateStart = 0
    collisionEnd = False
    collidingStateEnd = 0
    for i in range(len(states)):
        temp = pygame.Rect(states[i].pos[0] - stateSize / 2, states[i].pos[1] - stateSize / 2, stateSize, stateSize)
        startRect = pygame.Rect(activeTransition[0][0], activeTransition[0][1], 2, 2)
        endRect = pygame.Rect(activeTransition[1][0], activeTransition[1][1], 2, 2)
        if temp.colliderect(startRect):
            collisionStart = True
            collidingStateStart = i
        if temp.colliderect(endRect):
            collisionEnd = True
            collidingStateEnd = i
    if collisionStart and collisionEnd:
        print("New transition")
        temp = Transition(states[collidingStateStart], states[collidingStateEnd], [[activeTransition[0][0], activeTransition[0][1]], [activeTransition[1][0], activeTransition[1][1]]])
        if states[collidingStateStart] not in transitions:
            transitions[states[collidingStateStart]] = []
        transitions[states[collidingStateStart]].append(temp)
 
    elif collisionEnd:
        print("Start state")
    else:
        print("Invalid")
        #temp = Transition(

    
        
        #if states[collidingStateStart] in transitions:
            #transitions[states[collidingStateStart]].append(Transition

def save():
    pass

def load():
    pass

ctrlDown = False
shiftDown = False
while True:
    surface.fill(WHITE)
    drawFSM()
    update()
    for e in get():
        if e.type == QUIT:
            save()
            pygame.quit()
            sys.exit()
        if e.type == MOUSEBUTTONDOWN:
            if not ctrlDown and not shiftDown:
                addRemoveState(e)
            if ctrlDown:
                toggleAccepting(e)
            elif shiftDown:
                activeTransition.append(e.pos)
                activeTransition.append(e.pos)
                drawActiveTransition = True
        if e.type == KEYDOWN:
            if e.key == K_LCTRL or e.key == K_RCTRL:
                ctrlDown = True
            if e.key == K_LSHIFT or e.key == K_RSHIFT:
                shiftDown = True
        if e.type == KEYUP:
            if e.key == K_LCTRL or e.key == K_RCTRL:
                ctrlDown = False
            if e.key == K_LSHIFT or e.key == K_RSHIFT:
                shiftDown = False
                drawActiveTransition = False
                while len(activeTransition) > 0:
                    del(activeTransition[0])
        if e.type == MOUSEBUTTONUP:
            if drawActiveTransition:
                addTransition()
                drawActiveTransition = False
                while len(activeTransition) > 0:
                    del(activeTransition[0])
        if e.type == MOUSEMOTION:
            if drawActiveTransition:
                activeTransition[1] = e.pos
