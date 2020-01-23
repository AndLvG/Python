import os
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 300))
clock = pygame.time.Clock()
screen.fill((0, 0, 78))

image = pygame.image.load("data/gameover.png").convert()
x = - 600

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if x < 0:
        x += 20
        screen.blit(image, (x, 1))

    pygame.display.flip()
    clock.tick(10)
pygame.quit()
