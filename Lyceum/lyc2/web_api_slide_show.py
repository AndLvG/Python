import os
import sys

import pygame
import requests

points = [['Эйфелева башня', '2.294589,48.858278'], ['Пирамида Хеопса', '31.134148,29.979458'],
          ['Красная площадь', '37.620763,55.754093']]
map_file = "map.png"
current = -1


def show_slide(current):
    map_request = f"https://static-maps.yandex.ru/1.x/?ll={points[current][1]}&spn=0.005,0.005&l=sat"
    response = requests.get(map_request)
    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)
    with open(map_file, "wb") as file:
        file.write(response.content)


def draw_text(surf, text):
    font_name = pygame.font.match_font('Arial')
    font = pygame.font.Font(font_name, 32)
    text_surface = font.render(text, True, pygame.Color('yellow'))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (300, 10)
    surf.blit(text_surface, text_rect)


def prepare_slide():
    global current
    if current + 1 == 3:
        current = 0
    else:
        current += 1
    show_slide(current)
    screen.blit(pygame.image.load(map_file), (0, 0))
    draw_text(screen, points[current][0])


pygame.init()
screen = pygame.display.set_mode((600, 450))
pygame.display.set_caption("Слайд шоу интересных мест. Нажмите любую клавишу")
running = True
prepare_slide()

while running:
    for event in pygame.event.get():
        # проверка для закрытия окна
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
            running = False
        elif event.type == pygame.KEYDOWN:
            prepare_slide()

    pygame.display.flip()

pygame.quit()

# Удаляем за собой файл с изображением.
os.remove(map_file)
