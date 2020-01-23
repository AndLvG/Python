import os
import pygame

screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()


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


class Car(pygame.sprite.Sprite):
    image = load_image("car2.png", -1)

    def __init__(self, group):
        super().__init__(group)
        self.image = Car.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 250
        self.direction = 1

    def update(self, *args):
        self.rect.x = self.rect.x + self.direction
        if self.rect.x + self.rect.width >= 500:
            self.image = pygame.transform.flip(self.image, 1, 0)
            self.direction = -1
        if self.rect.x < 0:
            self.image = pygame.transform.flip(self.image, 1, 0)
            self.direction = 1


all_sprites = pygame.sprite.Group()
Car(all_sprites)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        all_sprites.update(event)
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(80)

pygame.quit()
