from random import randint

import pygame

pygame.init()
W = 300
H = 300
WHITE = (255, 255, 255)


class Car(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, 0))


sc = pygame.display.set_mode((W, H))
# координата x будет случайна
car1 = Car(randint(1, W), 'data/hero.png')
car1.rect.x, car1.rect.y = 100, 100
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                car1.rect.y -= 10
            if i.key == pygame.K_DOWN:
                car1.rect.y += 10
            if i.key == pygame.K_RIGHT:
                car1.rect.x += 10
            if i.key == pygame.K_LEFT:
                car1.rect.x -= 10
    sc.fill(WHITE)
    sc.blit(car1.image, car1.rect)
    pygame.display.update()
