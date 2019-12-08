import pygame

n = int(input())
k = int(input())
red, green, blue = (255, 0, 0), (0, 255, 0), (0, 0, 255)
if k % 3 == 0:
    colors = [blue, green, red]
elif k % 3 == 1:
    colors = [red, blue, green]
else:
    colors = [green, red, blue]
size = n
n += k * n - size

pygame.init()
screen = pygame.display.set_mode((300, 300))
c = 0
while k > c:
    pygame.draw.circle(screen, colors[c % 3], (n, n), n - c * size)
    c += 1
pygame.display.update()

while 1:
    pygame.time.delay(1000)
    for i in pygame.event.get():
        if i.type == pygame.QUIT: exit()
