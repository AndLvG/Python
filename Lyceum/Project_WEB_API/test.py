from requests import get, post, delete, put

# Получение работы
print(get('http://localhost:5000/api/jobs').json())
# print(get('http://localhost:5000/api/jobs/1').json())
# print(get('http://localhost:5000/api/jobs/999').json())
print(get('http://localhost:5000/api/jobs/aaa').json())

# Добавление
# print(post('http://localhost:5000/api/jobs').json())  # Пустой POST запрос
# print(post('http://localhost:5000/api/jobs',
#            json={'title': 'Заголовок'}).json())  # Неполный POST запрос
# print(post('http://localhost:5000/api/jobs',
#            json={
#                'team_leader': "text",
#                'job': 'job from json',
#                'work_size': 12,
#                'collaborators': "5, 6",
#                'start_date': '30-01-12',
#                'is_finished': False
#            }).json())  # POST запрос в котором номер team_leader строка
# print(post('http://localhost:5000/api/jobs',
#            json={
#                'team_leader': 6,
#                'job': 'job from json',
#                'work_size': 12,
#                'collaborators': "5, 6",
#                'start_date': '30-01-12',
#                'is_finished': False
#            }).json())  # Правильный POST запрос

# Удаление работы
# print(delete('http://localhost:5000/api/jobs/999').json())
# # работы с id = 999 нет в базе

# print(delete('http://localhost:5000/api/jobs/text').json())
# # id = text не число

# print(delete('http://localhost:5000/api/jobs/14').json())

# Изменение работы
# print(put('http://localhost:5000/api/jobs',
#            json={
#                'id': 999,
#                'team_leader': 6,
#                'job': 'job from json updated',
#                'work_size': 12,
#                'collaborators': "5, 6",
#                'start_date': '30-01-12',
#                'end_date': '30-01-20',
#                'is_finished': True
#            }).json())  # Несуществующий ID

# print(put('http://localhost:5000/api/jobs',
#            json={
#                'id': 13,
#                'team_leader': 6,
#                'job': 'job from json updated',
#                'work_size': 12,
#                'collaborators': "5, 6",
#                'start_date': '30-01-12',
#                'end_date': '30-01-20',
#                'is_finished': True
#            }).json())  # Правльный PUT запрос

# print(get('http://localhost:5000/api/jobs').json())  # Все работы