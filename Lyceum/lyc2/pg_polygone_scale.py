import pygame

array = input().split(', ')
arr = []
for el in array:
    el = el[1:-1]
    el = el.split(";")
    x, y = round(float(el[0].replace(",", "."))) + 251, round(float(el[1].replace(",", "."))) + 251
    x, y = round(float(el[0].replace(",", "."))), round(float(el[1].replace(",", ".")))
    arr.append([x, y])

pygame.init()
screen = pygame.display.set_mode((501, 501))
running = True
# surf = pygame.Surface((501, 501))
# surf.fill(pygame.Color('black'))
# pygame.draw.polygon(surf, (255, 255, 255), arr, 1)
scale = 1
new_arr = []

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

    new_arr.clear()
    for el in arr:
        if el[0] < 0:
            x = el[0] * scale + 251
        else:
            x = el[0] * scale + 251
        if el[1] < 0:
            y = el[1] * scale + 251
        else:
            y = el[1] * scale + 251
        new_arr.append([x, y])
    pygame.draw.polygon(screen, (255, 255, 255), new_arr, 1)

    # newSurf = pygame.transform.scale(surf, (501 * scale, 501 * scale))
    # newRect = newSurf.get_rect()
    # newRect.center = (251, 251)
    # screen.blit(newSurf, newRect)

    pygame.display.flip()
pygame.quit()

# (2;-1), (3,5;0,5), (4;-1), (5;0), (4;2), (2;1), (2;3), (4;5), (4;6), (2;5), (1;7), (1;8), (0;7), (0;9), (-1;7), (-2;8), (-2;7), (-3;7), (-2;6), (-4;6), (-3;5), (-4;5), (-3;4), (-5;4), (-4;3), (-5;3), (-4;2), (-6;2), (-5;1), (-6;1), (-5;0), (-6;0), (-5;-1), (-6;-2), (-4;-2), (-5;-3), (-3;-4), (-4;-5), (-2;-5), (-1;-6), (3;-6), (3;-5), (1;-5), (1;-4), (2;-3), (2;-1)