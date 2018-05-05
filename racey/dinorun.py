#!/usr/bin/python3
#https://pythonprogramming.net/pygame-crashing-objects/?completed=/drawing-objects-pygame-tutorial/
#https://www.cs.ucsb.edu/~pconrad/cs5nm/topics/pygame/drawing/

import pygame, time, random

pygame.init()

y_change = 0

display_width = 500
display_height = 400

black = (0,0,0)
white = (255,255,255)
red =   (255,0,0)
blue =  (0,0,255)
green = (0,255,0)

ground = (display_height * 0.8) + 43

# player_width = 50
# JUMP_POWER = 10
# GRAVITY = 1

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Dino Run')
clock = pygame.time.Clock()

playerImg = pygame.image.load('dino.png')

def playerPos(x,y):
    gameDisplay.blit(playerImg,(x,y))

def jump():
    y_change = -4
    return y_change

def checkPlayerPos():
    pass

def gameLoop():
    x = (display_width * 0.1)
    y = (display_height * 0.8)


    y_change = 0
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    gameExit = True
                    
                if event.key == pygame.K_UP:
                    y_change = jump()

                if event.key == pygame.K_DOWN:
                    y_change = 4
                    # print('Down button pressed. y =', y, 'y_change =', y_change)

                if event.key == pygame.K_SPACE:
                    x = (display_width * 0.1)
                    y = (display_height * 0.8)

            if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        y_change = 0

        y += y_change

        gameDisplay.fill(white)

        playerPos(x,y)
        pygame.draw.line(gameDisplay, green, [0, ground], [display_width, ground], 5)

        pygame.display.update()
        clock.tick(60)



gameLoop()
pygame.quit()
quit()
