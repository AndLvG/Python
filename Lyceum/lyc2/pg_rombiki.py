import pygame, math

k = int(input())
pygame.init()
size = (155, 155)
screen = pygame.display.set_mode(size)
screen.fill(pygame.Color('yellow'))

color = pygame.Color('orange')
katet = int(math.sqrt(k ** 2) / 2)

for i in range(0, size[1] - katet * 2, katet * 2):
    for j in range(0, size[0] - katet * 2, katet * 2):
        pygame.draw.polygon(screen, color,
                            [[j + katet, i], [j + 2 * katet, i + katet], [j + katet, i + 2 * katet], [j, i + katet]])
pygame.display.update()

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT: exit()
