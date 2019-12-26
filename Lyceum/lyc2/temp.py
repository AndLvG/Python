import pygame

array = input().split(', ')
arr = []
for el in array:
    el = el[1:-1]
    el = el.split(";")
    x, y = round(float(el[0].replace(",", "."))) + 251, round(float(el[1].replace(",", "."))) + 251
    arr.append([x, y])

pygame.init()
screen = pygame.display.set_mode((501, 501))
running = True

again_new = []
k = 1
while running:
    screen.fill(pygame.Color('black'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                k = 2
            elif event.button == 5:
                k = - 2
            for i in range(len(arr)):
                x, y = arr[i]
                if y - 251 > 0:
                    y += k
                else:
                    y -= k
                if x - 251 > 0:
                    x += k
                else:
                    x -= k
                arr[i] = x, y
    pygame.draw.polygon(screen, (255, 255, 255), arr, 1)
    pygame.display.flip()
pygame.quit()
