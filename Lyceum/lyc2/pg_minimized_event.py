import pygame

pygame.init()
sc = pygame.display.set_mode((200, 200))
sc.fill((0, 0, 0))

c = 0
f1 = pygame.font.Font(None, 100)
text1 = f1.render(str(c), 1, (180, 0, 0))

close = True
clock = pygame.time.Clock()

sc.blit(text1, (50, 50))
pygame.display.update()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.ACTIVEEVENT:
            if event.gain == 0 and event.state == 6:
                close = True
    if close:
        c += 1
        sc.fill((0, 0, 0))
        font = pygame.font.Font(None, 100)
        text1 = font.render(str(c), True, [255, 0, 0])
        sc.blit(text1, (85, 70))
        close = False
    clock.tick(60)
    pygame.display.flip()

