import pygame
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(11, 13), Vector2(11, 14), Vector2(11, 15)]
        self.direction = Vector2(1,0)

        from main import cell_size

        #head
        self.head_up = pygame.image.load("Graphics/head_up.png").convert_alpha()
        self.head_up = pygame.transform.scale(self.head_up, (cell_size, cell_size))
        self.head_down = pygame.image.load("Graphics/head_down.png").convert_alpha()
        self.head_down = pygame.transform.scale(self.head_down, (cell_size, cell_size))
        self.head_right = pygame.image.load("Graphics/head_right.png").convert_alpha()
        self.head_right = pygame.transform.scale(self.head_right, (cell_size, cell_size))
        self.head_left = pygame.image.load("Graphics/head_left.png").convert_alpha()
        self.head_left = pygame.transform.scale(self.head_left, (cell_size, cell_size))

        #tail
        self.tail_up = pygame.image.load("Graphics/tail_up.png").convert_alpha()
        self.tail_up = pygame.transform.scale(self.tail_up, (cell_size, cell_size))
        self.tail_down = pygame.image.load("Graphics/tail_down.png").convert_alpha()
        self.tail_down = pygame.transform.scale(self.tail_down, (cell_size, cell_size))
        self.tail_right = pygame.image.load("Graphics/tail_right.png").convert_alpha()
        self.tail_right = pygame.transform.scale(self.tail_right, (cell_size, cell_size))
        self.tail_left = pygame.image.load("Graphics/tail_left.png").convert_alpha()
        self.tail_left = pygame.transform.scale(self.tail_left, (cell_size, cell_size))

        #body
        self.body_v = pygame.image.load("Graphics/body_vertical.png").convert_alpha()
        self.body_v = pygame.transform.scale(self.body_v, (cell_size, cell_size))
        self.body_h = pygame.image.load("Graphics/body_horizontal.png").convert_alpha()
        self.body_h = pygame.transform.scale(self.body_h, (cell_size, cell_size))

        #curve
        self.body_tr = pygame.image.load("Graphics/body_topright.png")
        self.body_tr = pygame.transform.scale(self.body_tr, (cell_size, cell_size))
        self.body_tl = pygame.image.load("Graphics/body_topleft.png")
        self.body_tl = pygame.transform.scale(self.body_tl, (cell_size, cell_size))
        self.body_br = pygame.image.load("Graphics/body_bottomright.png")
        self.body_br = pygame.transform.scale(self.body_br, (cell_size, cell_size))
        self.body_bl = pygame.image.load("Graphics/body_bottomleft.png")
        self.body_bl = pygame.transform.scale(self.body_bl, (cell_size, cell_size))

    def draw_snake(self):
        self.update_head()
        self.update_tail()
        from main import cell_size, screen
        for index, block in enumerate(self.body):
            #creating rect for the current block
            x_pos = block.x * cell_size
            y_pos = block.y * cell_size
            body_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            #the head based on direction
            if index == 0:
                screen.blit(self.head, body_rect)

            #working on the tail
            elif index == len(self.body) - 1:
                screen.blit(self.tail, body_rect)

            #working on the body, by comparing the previous and next block location,
            #and by that figuring where snake is going
            else:
                prev = self.body[index - 1] - block
                next = self.body[index + 1] - block

                if prev.x == next.x: 
                    screen.blit(self.body_v, body_rect)
                elif prev.y == next.y:
                    screen.blit(self.body_h, body_rect)
                else:
                    if prev.x == -1 and next.y == -1 or prev.y == -1 and next.x == -1:
                        screen.blit(self.body_tl, body_rect)
                    if prev.y == 1 and next.x == 1 or prev.x == 1 and next.y == 1:
                        screen.blit(self.body_br, body_rect)
                    if prev.x == -1 and next.y == 1 or prev.y == 1 and next.x == -1:
                        screen.blit(self.body_bl, body_rect)
                    if prev.x == 1 and next.y == -1 or prev.y == -1 and next.x == 1:
                        screen.blit(self.body_tr, body_rect)



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


    def update_head(self):
        relation = self.body[0] - self.body[1]
        if relation == (1,0):    self.head = self.head_right
        if relation == (-1, 0):    self.head = self.head_left
        if relation == (0, 1):    self.head = self.head_down
        if relation == (0,-1):    self.head = self.head_up

    def update_tail(self):
        relation = self.body[-2] - self.body[-1]
        if relation == (1,0):    self.tail = self.tail_left
        if relation == (-1, 0):    self.tail = self.tail_right
        if relation == (0, 1):    self.tail = self.tail_up
        if relation == (0,-1):    self.tail = self.tail_down