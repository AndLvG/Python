import os
import sys

import pygame
import requests

stadiums = {'Лужники':'37.553759,55.715919', 'Спартак':'37.440621,55.818072','Динамо':'37.438222,55.763009'}

response = None
map_request = "https://static-maps.yandex.ru/1.x/?ll=37.620070,55.753630&l=map&pt=" #  pt=37.620070,55.753630,pmwtm1~37.64,55.76363,pmwtm99"
for key, val in stadiums.items():
    map_request += f'{val},comma~'
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
pygame.display.set_caption("Стадионы Москвы")
# Рисуем картинку, загружаемую из только что созданного файла.
screen.blit(pygame.image.load(map_file), (0, 0))
# Переключаем экран и ждем закрытия окна.
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()

# Удаляем за собой файл с изображением.
os.remove(map_file)