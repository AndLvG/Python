import pygame, math

pygame.init()
screen = pygame.display.set_mode((201, 201))

done = False
clock = pygame.time.Clock()
screen.fill(pygame.Color('black'))

surf = pygame.Surface((201, 201))
surf.fill(pygame.Color('black'))
x0 = y0 = 101
a = 70

xn1 = x0 - int(math.sin(math.radians(- 15)) * a)
yn1 = y0 - int(math.cos(math.radians(- 15)) * a)
xn2 = x0 - int(math.sin(math.radians(15)) * a)
yn2 = y0 - int(math.cos(math.radians(15)) * a)
pygame.draw.polygon(surf, pygame.Color('white'), [(x0, y0), (xn1, yn1), (xn2, yn2)], 0)

xn1 = x0 - int(math.sin(math.radians(120 - 15)) * a)
yn1 = y0 - int(math.cos(math.radians(120 - 15)) * a)
xn2 = x0 - int(math.sin(math.radians(120 + 15)) * a)
yn2 = y0 - int(math.cos(math.radians(120 + 15)) * a)
pygame.draw.polygon(surf, pygame.Color('white'), [(x0, y0), (xn1, yn1), (xn2, yn2)], 0)

xn1 = x0 - int(math.sin(math.radians(-120 - 15)) * a)
yn1 = y0 - int(math.cos(math.radians(-120 - 15)) * a)
xn2 = x0 - int(math.sin(math.radians(-120 + 15)) * a)
yn2 = y0 - int(math.cos(math.radians(-120 + 15)) * a)
pygame.draw.polygon(surf, pygame.Color('white'), [(x0, y0), (xn1, yn1), (xn2, yn2)], 0)

pygame.draw.circle(surf, pygame.Color('white'), (x0, y0), 10)
degree = angle = 0
fps = 600
v = 50  # градусов в секунду

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                angle += 1
            elif event.button == 3:
                angle -= 1

    rotatedSurf = pygame.transform.rotate(surf, degree)
    rotRect = rotatedSurf.get_rect()
    rotRect.center = (x0, y0)
    screen.blit(rotatedSurf, rotRect)

    degree += angle * v / fps
    if degree < 0:
        degree = 360
    clock.tick(fps)
    pygame.display.flip()

pygame.quit()
