"""date 20 September 2024
Worpies Snake version 2.0
Refactored based on Worpies Snake.py
And guidance found in https://medium.com/@glennlenormand/create-a-snake-game-in-python-using-oop-object-oriented-programming-484f039ebc8b

module used by main.py
"""

import pygame

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
SNAKE_BLOCK = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
    def create_snake(self):
        for position in STARTING_POSITIONS:
            pygame.draw.rect(screen, black, [position[0], position[1], SNAKE_BLOCK, SNAKE_BLOCK])
