import pygame
from pygame import draw

flag = True
flag2 = True
pygame.init()
size, coun = input().split()
rasdel = int(size) // int(coun)
screen = pygame.display.set_mode([int(size), int(size)])
screen.fill((255, 255, 255))

while pygame.event.wait().type != pygame.QUIT:
    for i in range(0, int(size), rasdel):
        for j in range(0, int(size), rasdel):
            if flag:
                draw.rect(screen, (0, 0, 0),
                          (i, j, i + rasdel, j + rasdel))
                flag = False
            else:
                flag = True
            pygame.display.flip()
    # if flag2:
    #     flag = False
    #     flag2 = False
    # else:
    #     flag = True
    #     flag2 = True
pygame.quit()