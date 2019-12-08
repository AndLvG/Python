import pygame
from pygame import draw

pygame.init()
size, coun = input().split()
rasdel = int(size) // int(coun)
screen = pygame.display.set_mode([int(size), int(size)])
white, black = (0, 255, 0), (0, 0, 0)
if int(coun) % 2 == 0:
    screen.fill(white)
    color = black
else:
    screen.fill(black)
    color = white

while pygame.event.wait().type != pygame.QUIT:
    for i in range(0, int(size), rasdel):
        for j in range(0, int(size), rasdel * 2):
            if i % (rasdel * 2) == 0:
                draw.rect(screen, color, (j + rasdel, i, rasdel, rasdel))
            else:
                draw.rect(screen, color, (j, i, rasdel, rasdel))
            pygame.display.flip()
pygame.quit()
