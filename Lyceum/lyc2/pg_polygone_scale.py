import pygame

array = input().split(', ')
arr = []
for el in array:
    el = el[1:-1]
    el = el.split(";")
    x, y = round(float(el[0].replace(",", "."))) + 251, round(float(el[1].replace(",", "."))) + 251
    arr.append([x, y])

pygame.init()
screen = pygame.display.set_mode((501, 501))
running = True
surf = pygame.Surface((501, 501))
surf.fill(pygame.Color('black'))
pygame.draw.polygon(surf, (255, 255, 255), arr, 1)
scale = 1

while running:
    screen.fill(pygame.Color('black'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                scale += 1
            elif event.button == 5 and scale > 1:
                scale -= 1

    newSurf = pygame.transform.scale(surf, (501 * scale, 501 * scale))
    newRect = newSurf.get_rect()
    newRect.center = (251, 251)
    screen.blit(newSurf, newRect)
    pygame.display.flip()
pygame.quit()
