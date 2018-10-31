#!/usr/bin/python3
#https://pythonprogramming.net/pygame-crashing-objects/?completed=/drawing-objects-pygame-tutorial/
#https://www.cs.ucsb.edu/~pconrad/cs5nm/topics/pygame/drawing/
import pygame
from pygame import *

WIN_WIDTH = 400 #Ширина создаваемого окна
WIN_HEIGHT = 320 # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT) # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = '#0639a8' # "#004400"
BLACK = (0,0,0)
WHITE = (255,255,255)
RED =   (255,0,0)
BLUE =  (0,0,255)
GREEN = (0,255,0)
GROUND = (WIN_HEIGHT * 0.8) + 43
WIDTH = 22
HEIGHT = 32
COLOR =  "#888888"
MOVE_SPEED = 7
JUMP_POWER = 10
GRAVITY = 0.35 # Сила, которая будет тянуть нас вниз

# player_width = 50
# JUMP_POWER = 10
# GRAVITY = 1
# gameDisplay = pygame.display.set_mode((display_width,display_height))
# pygame.display.set_caption('Dino Run')
# clock = pygame.time.Clock()
# playerImg = pygame.image.load('dino.png')

def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption('Dinorun')
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))
    bg.fill(Color(BACKGROUND_COLOR))
    timer = pygame.time.Clock()



    while True:
        timer.tick(60)
        up = False
        for e in pygame.event.get():
            if e.type == QUIT:
                raise SystemExit
            if e.type == KEYDOWN and e.key == K_q:
                raise SystemExit

            if e.type == KEYDOWN and e.key == K_UP:
                up = True

            if e.type == KEYUP and e.key == K_UP:
                up = False

        screen.blit(bg, (0,0))
        hero = Dino(50, 200)  # создаем героя по (x,y) координатам
        hero.update(up)  # передвижение
        hero.draw(screen)
        pygame.display.update()

class Dino(sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.startX = x
        self.startY = y
        self.xvel = 10
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?

    def update(self, up):
        if up:
            if self.onGround:
                self.yvel = -JUMP_POWER

        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False;  # Мы не знаем, когда мы на земле((
        self.rect.y += self.yvel
        self.rect.x += self.xvel

    def draw(self, screen):  # Выводим себя на экран
        screen.blit(self.image, (self.rect.x, self.rect.y))


if __name__ == '__main__':
    main()

# def gameLoop():
#     x = (display_width * 0.1)
#     y = (display_height * 0.8)
#
#
#     y_change = 0
#     gameExit = False
#
#     while not gameExit:
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
#
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_q:
#                     gameExit = True
#
#                 if event.key == pygame.K_UP:
#                     y_change = jump()
#
#                 if event.key == pygame.K_DOWN:
#                     y_change = 4
#                     # print('Down button pressed. y =', y, 'y_change =', y_change)
#
#                 if event.key == pygame.K_SPACE:
#                     x = (display_width * 0.1)
#                     y = (display_height * 0.8)
#
#             if event.type == pygame.KEYUP:
#                     if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
#                         y_change = 0
#
#             y += y_change
#
#         gameDisplay.fill(white)
#
#         playerPos(x,y)
#         pygame.draw.line(gameDisplay, green, [0, ground], [display_width, ground], 5)
#
#         pygame.display.update()
#         clock.tick(60)
#
#
#
# gameLoop()
# pygame.quit()
# quit()
