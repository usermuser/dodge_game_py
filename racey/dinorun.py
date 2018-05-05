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
red = (255,0,0)

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
        # pygame.draw.lines(gameDisplay, black, False, [(100,100), (150,200), (200,100)], 1)
        pygame.draw.lines(gameDisplay, red, False, [(100,100), (150,200), (200,100)], 1)
        pygame.draw.line(gameDisplay, black, [0, ((display_height * 0.8)+45)], [display_width, ((display_height * 0.8)+45)], 5)

        '''
         pygame.draw.line()
            draw a straight line segment
            line(Surface, color, start_pos, end_pos, width=1) -> Rect

            Draw a straight line segment on a Surface. There are no endcaps, the ends are squared off for thick lines.
        '''

        pygame.display.update()
        clock.tick(60)



gameLoop()
pygame.quit()
quit()
