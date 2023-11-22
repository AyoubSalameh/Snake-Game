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
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def eat(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_tail()

        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

    def draw_grass(self):
        dark_green = (0x57, 0xCC, 0x99)
        
        for col in range(cell_number):
            for row in range(cell_number):
                if (row + col) % 2 == 0:
                    grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                    pygame.draw.rect(screen, dark_green, grass_rect)

    def draw_score(self):
        score = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score, True, (0x13, 0x2A, 0x13))
        x_pos = (cell_number - 1) * cell_size - 10
        y_pos = (cell_number - 1) * cell_size - 10
        score_rect = score_surface.get_rect(topleft = (x_pos, y_pos))

        image = pygame.image.load("Graphics/apple.png").convert_alpha()
        #image = pygame.transform.scale(image, (35, 35))
        image_rect = image.get_rect(topright = (x_pos - 8, y_pos - 4))

        bg_rect = pygame.Rect(image_rect.left, image_rect.top, image_rect.width + score_rect.width + 15, image_rect.height)
        pygame.draw.rect(screen, (0x80, 0xED, 0x99), bg_rect)
        pygame.draw.rect(screen, (0x13, 0x2A, 0x13), bg_rect, 2)
        screen.blit(score_surface, score_rect)
        screen.blit(image, image_rect)

    def game_over(self):
        if not 0 <= self.snake.body[0].x < cell_number or \
        not 0 <= self.snake.body[0].y < cell_number \
        or self.snake.check_collision():
            main_game.game_over_screen()
            self.snake.body = [Vector2(9, 15), Vector2(9, 16), Vector2(9, 17)]
            self.snake.direction = Vector2(0,-1)


    def main_screen(self):

        title = "SNAKE GAME"
        title_surface = bold_font.render(title, True, (0x13, 0x2A, 0x13))
        x_pos = cell_number * cell_size // 2
        y_pos = cell_number * cell_size // 2 - 100
        title_rect = title_surface.get_rect(center = (x_pos, y_pos))

        instruction = "press SPACE to play"
        inst_surface = game_font.render(instruction, True, (0x13, 0x2A, 0x13))
        inst_rect = inst_surface.get_rect(center = (x_pos, x_pos + 100))


        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return
                    
            screen.fill((0x80, 0xED, 0x99))
            main_game.draw_elements()
            screen.blit(title_surface, title_rect)
            screen.blit(inst_surface, inst_rect)
            pygame.display.update()
            clock.tick(60)

    def game_over_screen(self):
        title = "GAME OVER"
        title_surface = bold_font.render(title, True, (0x13, 0x2A, 0x13))
        x_pos = cell_number * cell_size // 2
        y_pos = cell_number * cell_size // 2 - 100
        title_rect = title_surface.get_rect(center = (x_pos, y_pos))

        instruction = "press SPACE to play again"
        inst_surface = game_font.render(instruction, True, (0x13, 0x2A, 0x13))
        inst_rect = inst_surface.get_rect(center = (x_pos, x_pos + 100))


        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return
                    
            screen.fill((0x80, 0xED, 0x99))
            main_game.draw_elements()
            screen.blit(title_surface, title_rect)
            screen.blit(inst_surface, inst_rect)
            pygame.display.update()
            clock.tick(60)

    def play_screen(self):
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

        screen.fill((0x80, 0xED, 0x99))
        main_game.draw_elements()    
        pygame.display.update()
        clock.tick(60)


pygame.init()
cell_size = 35
cell_number = 20
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

game_font = pygame.font.Font('Graphics/pixelmix.ttf', 30)
bold_font = pygame.font.Font('Graphics/pixelmix_bold.ttf', 70)

main_game = MAIN()

#setting a timer, in order to move the snake
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game.main_screen()
while True:
    main_game.play_screen()