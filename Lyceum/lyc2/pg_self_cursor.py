import pygame

pygame.init()
screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption("Курсор")
pygame.mouse.set_visible(0)
done = False
clock = pygame.time.Clock()
Cursor = pygame.image.load('data/arrow.png')

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(pygame.Color('Black'))
    if pygame.mouse.get_focused():
        screen.blit(Cursor, pygame.mouse.get_pos())
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
