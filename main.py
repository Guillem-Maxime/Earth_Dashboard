import pygame

from dashboard import Dashboard

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

gameDisplay = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
#gameDisplay = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption('A bit Racey')

clock = pygame.time.Clock()

dashboard = Dashboard(SCREEN_WIDTH, SCREEN_HEIGHT, gameDisplay)

exited = False

while not exited:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exited = True
        print(event)

    gameDisplay.fill((255,255,255))
    dashboard.Update()
    pygame.display.update()
    clock.tick(60)