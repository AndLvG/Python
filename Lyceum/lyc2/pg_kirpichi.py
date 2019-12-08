import pygame

pygame.init()
screen = pygame.display.set_mode((300, 200))
screen.fill(pygame.Color('white'))

while pygame.event.wait().type != pygame.QUIT:
    for i in range(0, 200, 17):
        for j in range(0, 300, 32):
            if i % (17 * 2) == 0:
                pygame.draw.rect(screen, pygame.Color('red'), (j, i, 30, 15))
            else:
                pygame.draw.rect(screen, pygame.Color('red'), (j - 15, i, 30, 15))
            pygame.display.flip()
pygame.quit()
