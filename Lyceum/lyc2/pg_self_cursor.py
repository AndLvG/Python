import pygame

pygame.init()
screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption("Курсор")
pygame.mouse.set_visible(0)
done = False
clock = pygame.time.Clock()
Cursor = pygame.image.load('data/arrow.png')


def draw_cursor(screen, x, y):
    screen.blit(Cursor, (x, y))


while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(pygame.Color('Black'))
    pos = pygame.mouse.get_pos()
    x, y = pos[0], pos[1]
    draw_cursor(screen, x, y)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
