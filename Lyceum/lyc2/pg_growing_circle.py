import pygame

screen = pygame.display.set_mode((500, 500))
running = True
xpos = False
mous = False
x_pos = 0
y = 0
y_pos = 0
x = 0
rasmer = 0
fps = 30
screen.fill((0, 0, 255))
v = 10  # пикселей в секунду
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            mous = True
            xpos = True
        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
    if xpos:
        rasmer = 0
        x_pos, y_pos = x, y
        xpos = False
    if mous:
        screen.fill((0, 0, 255))
        pygame.draw.circle(screen, (255, 255, 0), (x_pos, y_pos), int(rasmer))
    rasmer += v / fps
    clock.tick(fps)
    pygame.display.flip()
    