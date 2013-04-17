'''This file has some important variables for the game'''
import pygame
from pygame import *

#For a better understanding of the code, visit http://www.pygame.org/news.html

pygame.init()

#size and screen are used to create the screen of the game
size = window_Width, window_Height = 800, 580 
screen = pygame.display.set_mode(size,0,32)

#Frames per second of the game
FPS = 60   
#nColorMax represents the total number of possible colors in the game
nColorMax = 3
#nFormMax represents the total number of possible forms in the game
nFormMax = 2
#colorFading is used to create a "fade in" effect to the game ending
colorFading = 0

'''For all the classes of this game that use color and/or form, the following
   order determines which number represents which color and which form.
   This order is determined by the order the images are organized in their
   respective directories.
   COLORS:
   color == 0: red        
   color == 1: green      
   color == 2: blue       
   color == 3: yellow
   FORMS:
   form == 0: circle
   form == 1: square
   form == 2: triangle
'''
