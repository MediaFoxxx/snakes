import pygame
import random

WIDTH = 800
HEIGHT = 600
FPS = 10
snake_block = 10

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake game")
clock = pygame.time.Clock()

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font_size = 35
score_font = pygame.font.SysFont("comicsansms", score_font_size)


def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, GREEN)
    screen.blit(value, [0, 8])


def our_snake(snake_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, BLACK, [x[0], x[1], snake_size, snake_size])


def message(msg, color):
    mes = font_style.render(msg, True, color)
    screen.blit(mes, [WIDTH / 6, HEIGHT / 2])


def game_loop():
    game_over = False
    game_close = False

    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    x1_change = 0
    y1_change = 0

    last_key = ' '
    snake_list = []
    snake_length = 1

    food_x = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(2*score_font_size, HEIGHT - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close == True:
            screen.fill(WHITE)
            message("You lost! Press Q-Quit or R-Play again", RED)
            pygame.draw.rect(screen, BLUE, [0, 0, WIDTH, 2*score_font_size])
            your_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and last_key != 'r':
                    x1_change = -snake_block
                    y1_change = 0
                    last_key = 'l'
                elif event.key == pygame.K_RIGHT and last_key != 'l':
                    x1_change = snake_block
                    y1_change = 0
                    last_key = 'r'
                elif event.key == pygame.K_UP and last_key != 'd':
                    x1_change = 0
                    y1_change = -snake_block
                    last_key = 'u'
                elif event.key == pygame.K_DOWN and last_key != 'u':
                    x1_change = 0
                    y1_change = snake_block
                    last_key = 'd'

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 2*score_font_size:
            print("border")
            game_close = True

        x1 += x1_change
        y1 += y1_change

        screen.fill(WHITE)
        pygame.draw.rect(screen, RED, [food_x, food_y, snake_block - 1, snake_block - 1])

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                print("snake")
                print(snake_list)
                game_close = True

        our_snake(snake_block, snake_list)
        pygame.draw.rect(screen, BLUE, [0, 0, WIDTH, 2*score_font_size])
        your_score(snake_length - 1)
        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(2*score_font_size, HEIGHT - snake_block) / 10.0) * 10.0
            snake_length += 1

        clock.tick(FPS)

    pygame.quit()
    quit()


if __name__ == "__main__":
    game_loop()
