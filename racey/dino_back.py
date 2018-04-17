#https://pythonprogramming.net/pygame-crashing-objects/?completed=/drawing-objects-pygame-tutorial/
import pygame, time, random

pygame.init()

display_width = 500
display_height = 400

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

player_width = 50
JUMP_POWER = 10
GRAVITY = 1

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Dino Run')
clock = pygame.time.Clock()

playerImg = pygame.image.load('dino.png')

def playerPos(x,y):
    gameDisplay.blit(playerImg,(x,y))

def gameLoop():
    x = (display_width * 0.5)
    y = (display_height * 0.5)
    print (x,y)

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
                    
                if event.key == pygame.K_SPACE:
                    y_change = 4

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE: # or event.key == pygame.K_RIGHT:
                        y_change = 0

        y = y_change

        gameDisplay.fill(white)

        playerPos(x,y)

        pygame.display.update()
        clock.tick(60)

gameLoop()
pygame.quit()
quit()
