import pygame
import pygame.locals
from pygame.locals import *
import math
import time

class GameObject(object):
    height = 10
    width = 10
    backgroundColor = (0, 0, 0)
        
    pos = None
    rect = None
    surface = None
    
    classification = None
    uniqueid = None

    def __init__(self, gameworld, pos):
    
        self.pos = pos
        
        self.uniqueid = time.time()
        
        self.rect = pygame.Rect(pos[0]-self.width/2, 
                pos[1]-self.height/2,
                self.width, 
                self.height)
                
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill(self.backgroundColor)
        
        gameworld.addobj(self)
        
    def draw(self, gameworld):
        gameworld.windowSurface.blit(self.surface, self.rect)
