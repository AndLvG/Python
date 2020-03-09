import os
import pygame

sc = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
pygame.display.set_caption('Platforms')
r = pygame.Rect(1, 2, 30, 20)


class Rect_main():
    def __init__(self, screen, rect):
        self.sc = screen
        self.rect = rect


class Platform(Rect_main):
    def draw(self):
        pygame.draw.rect(self.sc, pygame.Color('gray'), self.rect)


class Lesenka(Rect_main):
    def draw(self):
        pygame.draw.rect(self.sc, pygame.Color('red'), self.rect)


class Pers(Rect_main):
    def __init__(self, screen, rect):
        super(Pers, self).__init__(screen, rect)
        self.les = False

    def update(self):
        pygame.draw.rect(self.sc, pygame.Color('blue'), self.rect)
        if self.rect.top + self.rect.height < 500:
            flag = True
            for pl in platforms:
                if self.rect.colliderect(pl.rect):
                    flag = False
                    break
            for l in lesenki:
                if self.rect.colliderect(l.rect):
                    flag = False
                    self.les = True
                    break
                self.les = False
            if flag:
                self.rect.top += 5


platforms = []
lesenki = []
running = True
pers = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            if pygame.key.get_mods() & pygame.KMOD_CTRL:
                lesenki.append(Lesenka(sc, pygame.Rect(x, y, 10, 50)))
            else:
                platforms.append(Platform(sc, pygame.Rect(x, y, 50, 10)))
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            x, y = event.pos
            if pers == None:
                pers = Pers(sc, pygame.Rect(x, y, 20, 20))
            else:
                pers.rect.top = y
                pers.rect.left = x
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pers.rect.left -= 10
            elif event.key == pygame.K_RIGHT:
                pers.rect.left += 10
            elif event.key == pygame.K_UP and pers.les == True:
                pers.rect.top -= 10
            elif event.key == pygame.K_DOWN and pers.les == True:
                pers.rect.top += 10

    sc.fill((0, 0, 0))
    if pers != None:
        pers.update()
    for pl in platforms:
        pl.draw()
    for les in lesenki:
        les.draw()
    pygame.display.flip()
    clock.tick(10)

pygame.quit()
