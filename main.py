import pygame, sys
from fruit import FRUIT
from snake import SNAKE
from pygame.math import Vector2

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        
    def update(self):
        self.snake.move_snake()
        self.eat()
        self.game_over()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def eat(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_tail()

    def game_over(self):
        if not 0 <= self.snake.body[0].x < cell_number:
            pygame.quit()
            sys.exit()
        if not 0 <= self.snake.body[0].y < cell_number:
            pygame.quit()
            sys.exit()
        if self.snake.check_collision():
            pygame.quit()
            sys.exit()

pygame.init()
cell_size = 35
cell_number = 20
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

main_game = MAIN()

#setting a timer, in order to move the snake
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1,0)

    screen.fill((50, 140, 20))
    main_game.draw_elements()    
    pygame.display.update()
    clock.tick(60)