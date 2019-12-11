import pygame

pygame.init()
screen = pygame.display.set_mode((500, 400))
x_pos = 0
screen.fill((0, 0, 0))
running = True
x_pos = 0
v = 200   # пикселей в секунду
fps = 30
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            screen.fill((0, 0, 0))
            pygame.draw.circle(screen, (0, 0, 255), event.pos, 20)

    # screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (int(x_pos), 200), 20)
    x_pos += v / fps
    clock.tick(fps)
    if x_pos > 500:
        x_pos = 0
    pygame.display.flip()


pygame.quit()
