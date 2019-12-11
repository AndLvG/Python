import pygame

k = int(input())
pygame.init()
screen = pygame.display.set_mode((300, 300))
n = 300 // k // 2

for i in range(0, 150, n):
    pygame.draw.ellipse(screen, (255, 255, 255), (i, 0, 300 - i * 2, 300), 1)
    pygame.draw.ellipse(screen, (255, 255, 255), (0, i, 300, 300 - i * 2), 1)

pygame.display.update()

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT: exit()
