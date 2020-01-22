import pygame
import random
from os import path

img_dir = path.join(path.dirname(__file__), 'Data')

WIDTH = 1200
HEIGHT = 500
FPS = 30

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
pygame.display.set_caption("Platypus II")
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (50, 38))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.radius = 20
        self.rect.centery = HEIGHT / 2
        self.rect.left = 10
        self.speedy = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.speedy = -8
            self.rect.y += self.speedy
        if keystate[pygame.K_DOWN]:
            self.speedy = 8
            self.rect.y += self.speedy
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.y < 0:
            self.rect.y = 0

    def shoot(self):
        bullet = Bullet(self.rect.right,self.rect.centery )
        all_sprites.add(bullet)
        bullets.add(bullet)


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = random.choice(ufo_images)
        self.image_orig.set_colorkey(-1)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        self.rect.x = WIDTH +150
        self.rect.y = random.randrange(HEIGHT - self.rect.height)
        self.speedy = random.randrange(-1, 1)
        self.speedx = random.randrange(-12, -1)
        self.rot = 0
        self.rot_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        # self.rotate()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.x < -10 or self.rect.y < -25 or self.rect.bottom > HEIGHT + 20:
            self.rect.x = WIDTH +150
            self.rect.y = random.randrange(HEIGHT - self.rect.height)
            self.speedx =  random.randrange(-12, -1)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(bullet_img, (60, 30))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.centery = y
        self.speedy = 10

    def update(self):
        self.rect.x += self.speedy
        # убить, если он заходит за верхнюю часть экрана
        if self.rect.x > WIDTH:
            self.kill()


# Загрузка всей игровой графики
background = pygame.image.load(path.join(img_dir, "stars_background.png")).convert()
background_rect = background.get_rect()
player_img = pygame.image.load(path.join(img_dir, "platypus.png")).convert()
bullet_img = pygame.image.load(path.join(img_dir, "lazer.png")).convert()
ufo_images = []
for i in range(1, 13):
    ufo_images.append(pygame.transform.scale(pygame.image.load(path.join(img_dir, 'ufo'+str(i)+'.png')).convert(), (70, 50)))


all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(15):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # проверка для закрытия окна
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    # Обновление
    all_sprites.update()

    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

    # Проверка, не ударил ли моб игрока
    hits = pygame.sprite.spritecollide(player, mobs, False, pygame.sprite.collide_circle)
    if hits:
        running = False

    # Рендеринг
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
