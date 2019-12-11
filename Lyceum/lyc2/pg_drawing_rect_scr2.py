import pygame

pygame.init()
screen = pygame.display.set_mode((500, 400))
x_pos = 0
screen.fill((0, 0, 0))
running = True
screen2 = pygame.Surface(screen.get_size())
x1, y1, w, h = 0, 0, 0, 0
drawing = False  # режим рисования выключен
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True  # включаем режим рисования
            # запоминаем координаты одного угла
            x1, y1 = event.pos
        if event.type == pygame.MOUSEBUTTONUP:
            # сохраняем нарисованное (на втором холсте)
            screen2.blit(screen, (0, 0))
            drawing = False
        if event.type == pygame.MOUSEMOTION:
            # запоминаем текущие размеры
            w, h = event.pos[0] - x1, event.pos[1] - y1
    # рисуем на экране сохранённое на втором холсте
    screen.fill(pygame.Color('black'))
    screen.blit(screen2, (0, 0))
    if drawing:  # и, если надо, текущий прямоугольник
        pygame.draw.rect(screen, (0, 0, 255), ((x1, y1), (w, h)), 5)
    pygame.display.flip()


pygame.quit()
