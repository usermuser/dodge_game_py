#https://pythonprogramming.net/pygame-crashing-objects/?completed=/drawing-objects-pygame-tutorial/
import pygame, time, random

pygame.init()
display_width = 500
display_height = 400
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Dino Run')
clock = pygame.time.Clock()

dinoImg = pygame.image.load('dino.png')

def player(x,y):
    gameDisplay.blit(dinoImg,(x,y))

x = (display_width * 0.45)
y = (display_height * 0.8)

while not gameExit:

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                # if event.key == pygame.K_q:
                #     gameExit = True
                    
                if event.key == pygame.K_LEFT:
                    x_change= -4
                elif event.key == pygame.K_RIGHT:
                    x_change= 4
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

