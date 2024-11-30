#!/usr/bin/env python3

import pygame
import random
import time

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('SNEK')

SCREEN_COLOR = (0,0,0)
FOOD_COLOR = (255,255,255)
SNEK_COLOR = (0,255,0)
GO_TEXT = (255,0,0)
GRID_COLOR = (10,10,10)
clock = pygame.time.Clock()

item_size = 20
snake_speed = 10
snake_body = [(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)]
snake_direction = None

x,y = 0,0

def draw_grid():
    for x in range(0,SCREEN_WIDTH,item_size):
        pygame.draw.line(screen,GRID_COLOR,(x,0),(x,SCREEN_HEIGHT))
    for y in range(0,SCREEN_HEIGHT,item_size):
        pygame.draw.line(screen,GRID_COLOR,(0,y),(SCREEN_WIDTH,y))

def generate_food():
    return ( random.randint(0,(SCREEN_WIDTH-item_size) // item_size) * item_size,random.randint(0,(SCREEN_HEIGHT-item_size) // item_size)*item_size)
food_pos = generate_food()

font = pygame.font.SysFont('arialblack',55)

def game_over_msg():
    message = font.render('Game Over!', True, GO_TEXT)
    message_rect = message.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)) 
    screen.blit(message, message_rect)
    pygame.display.update()
    time.sleep(2)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake_direction != 'right':
                x,y = -item_size,0
                snake_direction = 'left'
            if event.key == pygame.K_RIGHT and snake_direction != 'left':
                x,y = item_size,0
                snake_direction = 'right'
            if event.key == pygame.K_UP and snake_direction != 'down':
                x,y = 0,-item_size
                snake_direction = 'up'
            if event.key == pygame.K_DOWN and snake_direction != 'up' :
                x,y = 0,item_size
                snake_direction = 'down'

    head = (snake_body[0][0] + x, snake_body[0][1] + y)
    snake_body.insert(0,head)
    snake_body.pop()

    if head[0] < 0 or head[0] >= SCREEN_WIDTH or head[1] < 0 or head[1] >= SCREEN_HEIGHT:
        running = False

    if snake_body[0] == food_pos:
        food_pos = generate_food()
        snake_body.append(snake_body[-1])
        snake_speed+=2

    screen.fill(SCREEN_COLOR)

    draw_grid()
    
    for segment in snake_body:
        pygame.draw.rect(screen,SNEK_COLOR,pygame.Rect(segment[0],segment[1],item_size,item_size))
    
    pygame.draw.rect(screen,FOOD_COLOR,pygame.Rect(food_pos[0], food_pos[1],item_size,item_size))

    pygame.display.update()

    clock.tick(snake_speed)

game_over_msg()
pygame.quit()