
import pygame
from pygame.locals import *
import time
import random

# Initialize Pygame
pygame.init()

# Define Colors
red = (255, 0, 0)
blue = (51, 153, 255)
grey = (192, 192, 192)
green = (51, 102, 0)
yellow = (0, 255, 255)

# Window dimensions
win_width = 600
win_height = 400
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Snake Game")
time.sleep(1)

# Snake settings
snake_size = 10
snake_speed = 10
clock = pygame.time.Clock()

# Fonts for text
font_style = pygame.font.SysFont("calibri", 26)
score_font = pygame.font.SysFont("comicsansms", 30)

# Function to display the score
def user_score(score):
    value = score_font.render("Score: " + str(score), True, red)
    window.blit(value, [0, 0])

# Function to draw the snake
def game_snake(snake_size, snake_length_list): 
    for x in snake_length_list:
        pygame.draw.rect(window, green, [x[0], x[1], snake_size, snake_size])

# Function to display messages like game over
def message(msg):
    msg = font_style.render(msg, True, red)
    window.blit(msg, [win_width / 6, win_height / 3])

# Main game loop function
def game_loop():
    gameOver = False
    gameClose = False

    # Initial position of the snake
    x1 = win_width / 2
    y1 = win_height / 2

    # Initial movement direction
    x1_change = 0
    y1_change = 0

    snake_length_list = []
    snake_length = 1

    # Random position for food
    foodx = round(random.randrange(0, win_width - snake_size) / 10.0) * 10.0
    foody = round(random.randrange(0, win_height - snake_size) / 10.0) * 10.0

    while not gameOver:

        while gameClose:
            window.fill(grey)
            message("You Lost! Press P to Play Again or Q to Quit")
            user_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = True
                        gameClose = True
                    if event.key == pygame.K_p:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.KEYDOWN:
                if event.key == K_LEFT:
                    x1_change = -snake_size
                    y1_change = 0
                if event.key == K_RIGHT:
                    x1_change = snake_size
                    y1_change = 0
                if event.key == K_UP:
                    x1_change = 0
                    y1_change = -snake_size
                if event.key == K_DOWN:
                    x1_change = 0
                    y1_change = snake_size

        # Check for boundary collision
        if x1 >= win_width or x1 < 0 or y1 >= win_height or y1 < 0:
            gameClose = True
        x1 += x1_change
        y1 += y1_change
        window.fill(grey)

        # Draw the food
        pygame.draw.rect(window, yellow, [foodx, foody, snake_size, snake_size])

        # Update snake position
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_length_list.append(snake_head)

        # Remove the snake tail if it exceeds the snake length
        if len(snake_length_list) > snake_length:
            del snake_length_list[0]

        # Draw the snake
        game_snake(snake_size, snake_length_list)

        # Update the score
        user_score(snake_length - 1)

        pygame.display.update()

        # Check if snake eats food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, win_width - snake_size) / 10.0) * 10.0
            foody = round(random.randrange(0, win_height - snake_size) / 10.0) * 10.0
            snake_length += 1

        # Set the snake speed
        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game loop
game_loop()
