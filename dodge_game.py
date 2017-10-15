import pygame

pygame.init()

display_width = 640
display_height = 480

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.quit:
            crashed = True

        print(event)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
