import pygame
from  pygame import draw

pygame.init()
color = pygame.Color(255, 255, 255)
width, height = input().split()
size = int(width), int(height)
screen = pygame.display.set_mode(size)

pygame.draw.rect(screen, color,
                 (1, 1, int(width) - 2, int(height) - 2), 0)

pygame.display.flip()

while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()