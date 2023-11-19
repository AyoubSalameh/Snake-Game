import pygame, sys

pygame.init()
width = 700
height = 700
screen = pygame.display.set_mode((width, height))

#in this while loop we draw all the elements and update them constantly
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()