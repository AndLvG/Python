import os
import pygame

sc = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
pygame.display.set_caption('Platforms')
r = pygame.Rect(1, 2, 30, 20)

class Platform():

    def __init__(self, screen, rect):
        self.sc = screen
        self.rect = rect

    def draw(self):
        pygame.draw.rect(self.sc, pygame.Color('gray'), self.rect)


class Pers():

    def __init__(self, screen, rect):
        self.sc = screen
        self.rect = rect

    def update(self):
        pygame.draw.rect(self.sc, pygame.Color('blue'), self.rect)
        if self.rect.top + self.rect.height < 500:
            self.rect.top += 50
        

platforms = []
running = True
pers = None
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            platforms.append(Platform(sc, pygame.Rect(x, y, 50, 10)))
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 and pers == None:
            x, y = event.pos
            pers = Pers(sc, pygame.Rect(x, y, 20, 20))

    sc.fill((0, 0, 0))
    if pers != None:
        pers.update()
    for pl in platforms:
        pl.draw()
    pygame.display.flip()
    clock.tick(1)

pygame.quit()
