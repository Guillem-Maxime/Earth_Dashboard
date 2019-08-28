import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('A bit Racey')

clock = pygame.time.Clock()

exited = False

while not exited:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exited = True
        print(event)

    pygame.display.update()
    clock.tick(60)