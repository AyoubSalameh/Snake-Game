import pygame, sys
from fruit import FRUIT

pygame.init()
cell_size = 35
cell_number = 20
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
screen.fill((20, 140, 200))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

fruit = FRUIT()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    fruit.draw_img()
    pygame.display.update()
    clock.tick(60)