import pygame, random
pygame.init()
screen = pygame.display.set_mode((500, 400))
for i in range(1000):
    screen.fill(pygame.Color('white'),
                (random.random() * 500,
                 random.random() * 400, 1, 1))
pygame.display.flip()
while 1:
    pygame.time.delay(1000)
    for i in pygame.event.get():
        if i.type == pygame.QUIT: exit()
