import pygame
import random

WIDTH = 800
HEIGHT = 600
FPS = 60

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snakes")
clock = pygame.time.Clock()


class Player1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 4
        self.rect.centery = HEIGHT / 2
        self.speedx = 0
        self.speedy = 0
        self.last_key = ' '
        self.length = 1
        self.stop = False

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > WIDTH or self.rect.left < 0 or self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.stop = True


class Player2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = 3 * WIDTH / 4
        self.rect.centery = HEIGHT / 2
        self.speedx = 0
        self.speedy = 0
        self.last_key = ' '
        self.length = 1
        self.stop = False

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > WIDTH or self.rect.left < 0 or self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.stop = True


class Food(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(0, WIDTH)
        self.rect.centery = random.randrange(0, HEIGHT)


def message(msg, color):
    mes = font_style.render(msg, True, color)
    screen.blit(mes, [WIDTH / 6, HEIGHT / 2])


font_style = pygame.font.SysFont("bahnschrift", 25)

all_sprites = pygame.sprite.Group()
player1 = Player1()
player2 = Player2()
all_sprites.add(player1)
all_sprites.add(player2)
apples = pygame.sprite.Group()
for i in range(2):
    f = Food()
    all_sprites.add(f)
    apples.add(f)

# Цикл игры
running = True
SPEED = 5
while running:
    while player1.stop == True or player2.stop == True:
        screen.fill(WHITE)
        message("You lost! Press Q-Quit or R-Play again", RED)
        #pygame.draw.rect(screen, BLUE, [0, 0, WIDTH, 2 * score_font_size])
        #ryour_score(snake_length - 1)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                    player1.stop = False
                    player2.stop = False
                if event.key == pygame.K_r:
                    player1 = Player1()
                    player2 = Player2()
                    all_sprites.add(player1)
                    all_sprites.add(player2)

                    screen.fill(WHITE)
                    all_sprites.draw(screen)
                    pygame.display.flip()

    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # проверка для закрытия окна
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and player1.last_key != 'r':
                player1.speedx = -SPEED
                player1.speedy = 0
                player1.last_key = 'l'
            elif event.key == pygame.K_d and player1.last_key != 'l':
                player1.speedx = SPEED
                player1.speedy = 0
                player1.last_key = 'r'
            elif event.key == pygame.K_w and player1.last_key != 'd':
                player1.speedx = 0
                player1.speedy = -SPEED
                player1.last_key = 'u'
            elif event.key == pygame.K_s and player1.last_key != 'u':
                player1.speedx = 0
                player1.speedy = SPEED
                player1.last_key = 'd'

            if event.key == pygame.K_LEFT and player2.last_key != 'r':
                player2.speedx = -SPEED
                player2.speedy = 0
                player2.last_key = 'l'
            elif event.key == pygame.K_RIGHT and player2.last_key != 'l':
                player2.speedx = SPEED
                player2.speedy = 0
                player2.last_key = 'r'
            elif event.key == pygame.K_UP and player2.last_key != 'd':
                player2.speedx = 0
                player2.speedy = -SPEED
                player2.last_key = 'u'
            elif event.key == pygame.K_DOWN and player2.last_key != 'u':
                player2.speedx = 0
                player2.speedy = SPEED
                player2.last_key = 'd'
    # Обновление
    all_sprites.update()

    # Проверка, не ударил ли моб игрока
    eat = pygame.sprite.spritecollide(player1, apples, True)
    if eat:
        f = Food()
        all_sprites.add(f)
        apples.add(f)
        player1.length += 1
    eat = pygame.sprite.spritecollide(player2, apples, True)
    if eat:
        f = Food()
        all_sprites.add(f)
        apples.add(f)
        player2.length += 1

    # Рендеринг
    screen.fill(WHITE)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()


if __name__ == "__main__":
    pygame.quit()
