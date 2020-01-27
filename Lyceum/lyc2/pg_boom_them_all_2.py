import os
import random

import pygame

screen = pygame.display.set_mode((500, 500))


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Bomb(pygame.sprite.Sprite):
    image = load_image("bomb.png")
    image_boom = load_image("boom.png")

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(500 - self.rect.width)
        self.rect.y = random.randrange(500 - self.rect.height)

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            self.image = self.image_boom


all_sprites = pygame.sprite.Group()
bombs = pygame.sprite.Group()
for i in range(10):
    flag = True
    while flag:
        b = Bomb()
        hits = pygame.sprite.spritecollide(b, bombs, False, pygame.sprite.collide_circle)
        if len(hits) == 0:
            all_sprites.add(b)
            bombs.add(b)
            flag = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        all_sprites.update(event)
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()

pygame.quit()
