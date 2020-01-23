import pygame
import random
from os import path

img_dir = path.join(path.dirname(__file__), 'data\img')
snd_dir = path.join(path.dirname(__file__), 'data\snd')
explode_dir = path.join(path.dirname(__file__), 'data\explodes')

WIDTH = 1200
HEIGHT = 500
FPS = 30
# Сколько захватчиков
ufos = 15

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
pygame.display.set_icon(pygame.image.load(path.join(img_dir, "platypus.png")))
clock = pygame.time.Clock()

font_name = pygame.font.match_font('Verdana')


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, YELLOW)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (70, 45))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.radius = 20
        self.rect.centery = HEIGHT / 2
        self.rect.left = 10
        self.speedy = 0
        self.speedx = 0
        self.shield = 100

    def update(self):
        self.speedy = 0
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.speedy = -8
            self.rect.y += self.speedy
        if keystate[pygame.K_DOWN]:
            self.speedy = 8
            self.rect.y += self.speedy
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
            self.rect.x += self.speedx
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
            self.rect.x += self.speedx
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH


    def shoot(self):
        bullet = Bullet(self.rect.right, self.rect.centery)
        all_sprites.add(bullet)
        bullets.add(bullet)
        shot.play()


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = random.choice(ufo_images)
        self.image_orig.set_colorkey(-1)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        self.rect.x = WIDTH + 150
        self.rect.y = random.randrange(HEIGHT - self.rect.height)
        self.speedy = random.randrange(-1, 1)
        self.speedx = random.randrange(-12, -1)
        self.last_update = pygame.time.get_ticks()


    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.x < -10 or self.rect.y < -25 or self.rect.bottom > HEIGHT + 20:
            self.rect.x = WIDTH + 150
            self.rect.y = random.randrange(HEIGHT - self.rect.height)
            self.speedx = random.randrange(-12, -1)


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
        # убить, если он заходит за правую часть экрана
        if self.rect.x > WIDTH:
            self.kill()


class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

def HP(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 70
    BAR_HEIGHT = 6
    fill = (pct / 100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 1)

def newmob():
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

def start_screen():
    screen.blit(background, background_rect)
    draw_text(screen, "Platypus II", 64, WIDTH / 2, HEIGHT / 4)
    draw_text(screen, "Стрелками двигай пробелом стреляй", 22,
              WIDTH / 2, HEIGHT / 2)
    draw_text(screen, "Нажми любую клавишу", 18, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False

# Загрузка всей игровой графики
background = pygame.image.load(path.join(img_dir, "stars_background.png")).convert()
background_rect = background.get_rect()
player_img = pygame.image.load(path.join(img_dir, "platypus.png")).convert()
bullet_img = pygame.image.load(path.join(img_dir, "lazer.png")).convert()
# Захватчики
ufo_images = []
for i in range(1, 13):
    ufo_images.append(
        pygame.transform.scale(pygame.image.load(path.join(img_dir, 'ufo{}.png'.format(i))).convert(), (70, 50)))
# Взрывы
explosion_anim = {}
explosion_anim['lg'] = []
explosion_anim['sm'] = []
for i in range(9):
    filename = 'regularExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join(explode_dir, filename)).convert()
    img.set_colorkey(BLACK)
    img_lg = pygame.transform.scale(img, (75, 75))
    explosion_anim['lg'].append(img_lg)
    img_sm = pygame.transform.scale(img, (32, 32))
    explosion_anim['sm'].append(img_sm)
# Звуки
shot = pygame.mixer.Sound(path.join(snd_dir, 'shot.wav'))
explode = pygame.mixer.Sound(path.join(snd_dir, 'explode.wav'))
explode_player = pygame.mixer.Sound(path.join(snd_dir, 'explode_player.wav'))

pygame.mixer.music.load(path.join(snd_dir, 'fon_music.ogg'))
pygame.mixer.music.set_volume(0.4)

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(ufos):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

score = 0
ufo = 0
best_score = 0
# Цикл игры
pygame.mixer.music.play(loops=-1)
game_over = True
running = True

while running:
    if game_over:
        start_screen()
        game_over = False
        all_sprites = pygame.sprite.Group()
        mobs = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        # powerups = pygame.sprite.Group()
        player = Player()
        all_sprites.add(player)
        for i in range(ufos):
            newmob()
        score = 0
        ufo = 0
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # проверка для закрытия окна
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    # Обновление
    all_sprites.update()

    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        score += 50 - hit.radius
        ufo += 1
        m = Mob()
        all_sprites.add(m)
        expl = Explosion(hit.rect.center, 'lg')
        all_sprites.add(expl)
        mobs.add(m)
        explode.play()

    # Проверка, не ударил ли моб игрока
    hits = pygame.sprite.spritecollide(player, mobs, False, pygame.sprite.collide_circle)
    for hit in hits:
        player.shield -= 20

        m = Mob()
        all_sprites.add(m)
        mobs.add(m)
        explode_player.play()
        expl = Explosion(hit.rect.center, 'sm')
        all_sprites.add(expl)
        hit.kill()
        if player.shield <= 0:
            game_over = True
            if score > best_score:
                best_score = score

    # Рендеринг
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    draw_text(screen, f'Сбито захватчиков {ufo}, Счёт {str(score)}, Лучший результат {best_score}', 18, WIDTH / 2, 10)

    HP(screen, player.rect.x, player.rect.y + 45, player.shield)
    pygame.display.flip()

pygame.quit()
