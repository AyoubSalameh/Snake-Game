import pygame
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(11, 13), Vector2(11, 14), Vector2(11, 15)]
        self.direction = Vector2(1,0)

    def draw_snake(self):
        from main import cell_size, screen
        for block in self.body:
            x_pos = block.x * cell_size
            y_pos = block.y * cell_size
            body_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, (140,10,130), body_rect)

    def move_snake(self):
        body_copy = self.body[:-1]  #the last element is removed
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]

    def add_tail(self):
        body_copy = self.body[:]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]

    def check_collision(self):
        for block in self.body[1:]:
            if block == self.body[0]:
                return True


