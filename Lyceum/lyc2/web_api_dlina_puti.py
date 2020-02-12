import os
import sys

import pygame
import requests

import distance

points = ['30.304766,59.939517', '30.273474,59.929367', '30.261972,59.917065', '30.071928,59.916731',
          '29.904905,59.889461']

dist = 0
for i in range(len(points) - 1):
    dist += distance.lonlat_distance(map(float, points[i].split(',')), map(float, points[i + 1].split(',')))

print(int(dist))

response = None
map_request = "https://static-maps.yandex.ru/1.x/?l=map&ll=30.089428,59.918785&pl="
for p in points:
    map_request += f'{p},'
map_request = map_request[:-1]
print(map_request)
response = requests.get(map_request)

if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

# Запишем полученное изображение в файл.
map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

def draw_text(surf, text):
    font_name = pygame.font.match_font('Arial')
    font = pygame.font.Font(font_name, 32)
    text_surface = font.render(text, True, pygame.Color('blue'))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (300, 10)
    surf.blit(text_surface, text_rect)

# Инициализируем pygame
pygame.init()
screen = pygame.display.set_mode((600, 450))
pygame.display.set_caption("Длина пути Эрмитаж - Петергоф")
# Рисуем картинку, загружаемую из только что созданного файла.
screen.blit(pygame.image.load(map_file), (0, 0))
draw_text(screen, f'Общая длина пути: {int(dist)} метров')
# Переключаем экран и ждем закрытия окна.
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()

# Удаляем за собой файл с изображением.
os.remove(map_file)
