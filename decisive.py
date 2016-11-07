

import pygame,sys                        # needeed to import pygame and sys module
from pygame.locals import *              #  contains several constant variables that are easy to identify as being in the pygame.locals module without pygame.locals. i

                               # Surface objects refer to 2-D immages
pygame.init()               #initialising pygame module
FPS= 30
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((400, 300)) # returns the pygame.Surface object for window.This functions tell (width,height) of window in pixels
pygame.display.set_caption('Game!')#making text appears as caption of the window

White = (255,255,255)






