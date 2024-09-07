"""date 16 August 2024
Worpies Snake version
based on code provided by https://www.edureka.co/blog/snake-game-with-pygame/
"""

# import pygame (set of cross module Python codes that is designed to program
# video games using python language

import pygame
import time         # built-in module
import random       # built-in module

# initializes all of the imported Pygame modules
# (returns a tuple indicating success and failure of initializations)
pygame.init()

# initialize colours used in game. Pygame uses RGB colour scheme
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

# initialize display
dis_width = 800
dis_height  = 600
screen = pygame.display.set_mode((dis_width,dis_height)) # creates the screen
pygame.display.set_caption('Worpies Snaky') #sets the screen title

# using the pygame inbuilt clok funtion
clock = pygame.time.Clock()

snake_block = 20
snake_speed = 10

font_style = pygame.font.SysFont(None, 50)

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [100 , dis_height/2])

# update method used to update any changes made to the screen
# .flip() method works very similar to .update()
# update() method updates only the changes that are made
# (however, if no parameters are passed, updates the complete screen)
# but the flip() method redoes the complete screen again.
# (code disabled, because the screen is updated in the while loop)
# pygame.display.update()

x1_change = 0
y1_change = 0

game_over = False

def gameLoop():  # creating a function
    game_over = False
    game_close = False
 
    # starting coordinates of the snake
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10) *10    # /10 and *10 to ensure coordinates are rounded to nearest decimal
    foody = round(random.randrange(0, dis_height - snake_block) / 10) *10   # as snake coordinates also only uses decimals
 
    while not game_over:
 
        while game_close == True:
            screen.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_speed
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_speed
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_speed
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_speed
                    x1_change = 0
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
 
        x1 += x1_change
        y1 += y1_change
        screen.fill(white)
        pygame.draw.rect(screen, red, [foodx, foody, snake_block, snake_block])
        pygame.draw.rect(screen, black, [x1, y1, snake_block, snake_block])
        pygame.display.update()
        print("foodx:",foodx," x1:",x1," - foody:", foody, " y1:", y1)
 
        if int(x1) == foodx and int(y1) == foody:
            message("Yummy!!", blue)
            pygame.display.update()
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()