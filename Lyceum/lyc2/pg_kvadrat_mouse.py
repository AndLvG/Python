import pygame

pygame.init()
sc = pygame.display.set_mode((300, 300))
x = y = 0
square = pygame.Rect(0, 0, 100, 100)

while True:
    e = pygame.event.wait()
    if e.type == pygame.QUIT:
        break
    elif e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
        if square.collidepoint(e.pos):
            x = square.centerx - e.pos[0]
            y = square.centery - e.pos[1]
    elif e.type == pygame.MOUSEMOTION and e.buttons[0] and square.collidepoint(e.pos):
        square.centerx = e.pos[0] + x
        square.centery = e.pos[1] + y
    sc.fill((0, 0, 0))
    pygame.draw.rect(sc, pygame.Color('green'), square)
    pygame.display.flip()
pygame.quit()
