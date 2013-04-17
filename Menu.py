'''This file loads all the images used on the menu screen'''
import pygame, glob
from pygame import *
from gameSettings import *

#For a better understanding of the code, visit http://www.pygame.org/news.html 

pygame.init()

#objects_Menu is a list containing all the images of png format
objects_Menu = glob.glob("C:/Meggido/Arts/Menu/*png")

#playButton is a Pygame.Surface that contains a image
playButton = pygame.image.load(objects_Menu[0])
#Variables to set the position of the Pygame.Surface
playButtonX, playButtonY = ((0.3)*window_Width, window_Height/2)
#Rect of the Pygame.Surface (used for collision)
playButtonrect = playButton.get_rect(topleft = (playButtonX, playButtonY))

#quitButton is a Pygame.Surface that contains a image
quitButton = pygame.image.load(objects_Menu[1])
#Variables to set the position of the Pygame.Surface
quitButtonX, quitButtonY = ((0.6)*window_Width, window_Height/2)
#Rect of the Pygame.Surface (used for collision)
quitButtonrect = quitButton.get_rect(topleft = (quitButtonX, quitButtonY))

def draw_playButton():
    '''Draws the play button on the screen.
    '''
    screen.blit(playButton, playButtonrect)

def draw_quitButton():
    '''Draws the quit button on the screen.
    '''
    screen.blit(quitButton, quitButtonrect)
