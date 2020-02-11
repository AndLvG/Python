import os
import sys

import pygame
import requests

points = ['30.304766,59.939517', '30.273474,59.929367','30.261972,59.917065','30.071928,59.916731','29.904905,59.889461']

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

# Инициализируем pygame
pygame.init()
screen = pygame.display.set_mode((600, 450))
pygame.display.set_caption("Маршрут Эрмитаж - Петергоф")
# Рисуем картинку, загружаемую из только что созданного файла.
screen.blit(pygame.image.load(map_file), (0, 0))
# Переключаем экран и ждем закрытия окна.
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()

# Удаляем за собой файл с изображением.
os.remove(map_file)