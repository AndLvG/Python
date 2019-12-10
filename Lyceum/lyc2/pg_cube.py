import pygame

w, h = map(int, input().split())

pygame.init()
screen = pygame.display.set_mode((300, 300))
screen.fill(pygame.Color('black'))

while pygame.event.wait().type != pygame.QUIT:
    color = pygame.Color('red')
    hsva = color.hsva
    hsv = (h, hsva[1], hsva[2], hsva[3])
    color.hsva = hsv
    #  Верхняя грань
    pygame.draw.polygon(screen, color,
                        [[150 - int(w / 2), 150], [150, 150 - int(w / 2)], [150 + w, 150 - int(w / 2)],
                         [150 + int(w / 2), 150]])
    # Передняя грань
    color.hsva = (hsv[0], hsv[1], 75, hsv[3])
    pygame.draw.rect(screen, color, (150 - int(w / 2), 150, w, w))

    #  Боковая грань
    color.hsva = (hsv[0], hsv[1], 50, hsv[3])
    pygame.draw.polygon(screen, color,
                        [[150 + int(w / 2), 150], [150 + w, 150 - int(w / 2)], [150 + w, 150 + int(w / 2)],
                         [150 + int(w / 2), 150 + w]])

    pygame.display.update()
pygame.quit()
