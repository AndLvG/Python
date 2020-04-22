import pytest
from requests import get, post, delete, put

# Получение всех пользователей
print(get('http://localhost:5000/api/v2/users').json())
# Получение одного пользователя
print(get('http://localhost:5000/api/v2/users/1').json())
# Несуществующий пользователь
print(get('http://localhost:5000/api/v2/users/999').json())
# Вместо id пользователя строка
print(get('http://localhost:5000/api/v2/users/aaa').json())

# Добавление
print(post('http://localhost:5000/api/v2/users').json())  # Пустой POST запрос
print(post('http://localhost:5000/api/v2/users',
           json={'title': 'Заголовок'}).json())  # Неполный POST запрос
print(post('http://localhost:5000/api/v2/users',
           json={
               'user_id': 'user_id0',
               'surname': 'surname',
               'name': 'name',
               'age': 'age',
               'position': 'position',
               'speciality': 'speciality',
               'address': 'address',
               'email': 'email',
               'password': 'p'
           }).json())  # POST запрос в котором id строка
print(post('http://localhost:5000/api/v2/users',
           json={
               'user_id': '20',
               'surname': 'surname',
               'name': 'name',
               'age': '30',
               'position': 'position',
               'speciality': 'speciality',
               'address': 'address',
               'email': 'email',
               'password': 'p'
           }).json())  # Правильный POST запрос

# Удаление 
print(delete('http://localhost:5000/api/v2/users/999').json())
# id = 999 нет в базе
print(delete('http://localhost:5000/api/v2/users/text').json())
# id = text не число
print(delete('http://localhost:5000/api/v2/users/20').json())

# Изменение
print(put('http://localhost:5000/api/v2/users/999',
           json={
                'user_id': '999',
               'surname': 'surname',
               'name': 'name',
               'age': '30',
               'position': 'position',
               'speciality': 'speciality',
               'address': 'address',
               'email': 'email',
               'password': 'p'
           }).json())  # Несуществующий ID

print(put('http://localhost:5000/api/v2/users/20',
           json={
                'user_id': '20',
               'surname': 'surname',
               'name': 'name',
               'age': '30',
               'position': 'position2',
               'speciality': 'speciality',
               'address': 'address',
               'email': 'email',
               'password': 'p'
           }).json())  # Правльный PUT запрос

print(get('http://localhost:5000/api/v2/users').json())  # Все работы
