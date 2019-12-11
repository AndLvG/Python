import pygame, math

pygame.init()
screen = pygame.display.set_mode((201, 201))

degree = 0
done = False
clock = pygame.time.Clock()
screen.fill(pygame.Color('black'))

surf = pygame.Surface((201, 201))
surf.fill(pygame.Color('black'))
# surf.set_colorkey((255, 0, 0))
x0 = y0 = 101
a = 70
b = int(a * math.sin(math.radians(30) / 2))

x1 = x0 - b
x2 = x0 + b
y1 = y2 = y0 - int(math.sqrt(a ** 2 - b ** 2))
pygame.draw.polygon(surf, pygame.Color('white'), [(x0, y0), (x1, y1), (x2, y2)], 0)

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

while not done:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    rotatedSurf = pygame.transform.rotate(surf, degree)
    rotRect = rotatedSurf.get_rect()
    rotRect.center = (x0, y0)
    screen.blit(rotatedSurf, rotRect)

    degree += 5
    if degree < 0:
        degree = 360

    pygame.display.flip()

pygame.quit()
