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
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# initialize display
dis_width = 600
dis_height  = 400
screen = pygame.display.set_mode((dis_width,dis_height)) # creates the screen
pygame.display.set_caption('Worpies Snaky') #sets the screen title

# using the pygame inbuilt clok funtion
clock = pygame.time.Clock()

snake_block = 20
snake_movement = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsans", 35)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])
 
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [dis_width / 4 , dis_height / 2])

# update method used to update any changes made to the screen
# .flip() method works very similar to .update()
# update() method updates only the changes that are made
# (however, if no parameters are passed, updates the complete screen)
# but the flip() method redoes the complete screen again.
# (code disabled, because the screen is updated in the while loop)
# pygame.display.update()

def gameLoop():
    game_over = False
    game_close = False

    # starting coordinates of the snake
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    # starting movement of the snake, when both x1_change and y1_change = 0, snake does
    # not move at the start of the game
    #x1_change = 0
    #y1_change = 0
    movement = random.choice([10, -10])
    if random.choice(["x", "y"]) == "x":
        x1_change = movement
        y1_change = 0
    else:
        x1_change = 0
        y1_change = movement

    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            screen.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
 
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
                    x1_change = -snake_movement
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_movement
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_movement
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_movement
                    x1_change = 0
        print(event.type, x1_change, y1_change)

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(blue)
        pygame.draw.rect(screen, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
 
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
        
        #print("x1:", x1," x2:", y1," foodx:", foodx," foody:", foody," snake_head:", snake_Head)

        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()