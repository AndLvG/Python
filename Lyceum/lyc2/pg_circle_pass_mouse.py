import pygame

screen = pygame.display.set_mode((501, 501))
running = True
x_krug = 250
y_krug = 250
xpos = False
pygame.draw.circle(screen, (255, 0, 0), (x_krug, y_krug), 20)
x_pos = 250
y = 250
y_pos = 250
x = 250
screen.fill((0, 0, 0))
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            xpos = True
        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
    if xpos:
        rasmer = 0
        x_pos, y_pos = x, y
        xpos = False
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (x_krug, y_krug), 20)
    if y_krug < y_pos:
        y_krug += 1
    elif y_krug == y_pos:
        y_krug = y_krug
    else:
        y_krug -= 1
    if x_krug < x_pos:
        x_krug += 1
    elif x_krug == x_pos:
        x_krug = x_krug
    else:
        x_krug -= 1
    clock.tick(60)
    pygame.display.flip()