import pygame, random
from pygame.math import Vector2

class FRUIT:
    def __init__(self) -> None:
        from main import cell_number
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self):
        from main import cell_size, screen
        fruit_rect = pygame.Rect(self.x * cell_size, self.y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, pygame.Color('red'), fruit_rect)

    def draw_img(self):
        from main import cell_size, screen
        image = pygame.image.load("strawberry.png").convert_alpha()
        image = pygame.transform.scale_by(image, 0.03)
        straw_rect = image.get_rect()
        straw_rect.topleft = self.x * cell_size, self.y * cell_size
        screen.blit(image, straw_rect)