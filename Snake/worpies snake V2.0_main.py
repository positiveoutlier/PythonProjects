"""date 20 September 2024
Worpies Snake version 2.0
Refactored based on Worpies Snake.py
And guidance found in https://medium.com/@glennlenormand/create-a-snake-game-in-python-using-oop-object-oriented-programming-484f039ebc8b
"""

# import pygame (set of cross module Python codes that is designed to program # video games using python language)

import pygame
from time import sleep
import random

# initializes all of the imported Pygame modules
# (returns a tuple indicating success and failure of initializations)
pygame.init()

# initialize colours used in game. Pygame uses RGB colour scheme
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# initialize display
dis_width = 600
dis_height  = 400
screen = pygame.display.set_mode((dis_width,dis_height)) # creates the screen
pygame.display.set_caption('Worpies Snakey_refactored') #sets the screen title
