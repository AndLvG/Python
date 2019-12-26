import pygame


class Rect:
    def __init__(self, screen, rect):
        self.sc = screen
        self.rect = rect

    def draw(self):
        pygame.draw.rect(self.sc, pygame.Color('white'), self.rect, 2)


pygame.init()
sc = pygame.display.set_mode((500, 500))
running = True
sc.fill((0, 0, 0))
pygame.display.set_caption('Rects')
drawing = False
rects = []
x_start = y_start = x = y = 0

while True:
    e = pygame.event.wait()
    if e.type == pygame.QUIT:
        break
    elif e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
        x_start, y_start = e.pos
        drawing = True
    elif e.type == pygame.MOUSEMOTION:
        if drawing:
            x, y = e.pos
    elif e.type == pygame.MOUSEBUTTONUP:
        rects.append(Rect(sc, (x_start, y_start, x - x_start, y - y_start)))
        drawing = False
    elif e.type == pygame.KEYDOWN and e.key == pygame.K_z:
        if pygame.key.get_mods() & pygame.KMOD_CTRL:
            rects.pop()

    sc.fill((0, 0, 0))
    if drawing:
        pygame.draw.rect(sc, pygame.Color('white'), (x_start, y_start, x - x_start, y - y_start), 2)
    for rect in rects:
        rect.draw()
    pygame.display.flip()
pygame.quit()
