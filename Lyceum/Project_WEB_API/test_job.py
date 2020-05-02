from requests import get, post, delete, put

# Получение всех 
print(get('http://localhost:5000/api/v2/jobs').json())
# Получение одного 
print(get('http://localhost:5000/api/v2/jobs/1').json())
# Несуществующий 
print(get('http://localhost:5000/api/v2/jobs/999').json())
# Вместо id  строка
print(get('http://localhost:5000/api/v2/jobs/aaa').json())

# Добавление
print(post('http://localhost:5000/api/v2/jobs').json())  # Пустой POST запрос
print(post('http://localhost:5000/api/v2/jobs',
           json={'title': 'Заголовок'}).json())  # Неполный POST запрос
print(post('http://localhost:5000/api/v2/jobs',
           json={
               'job_id': 'a',
               'team_leader': "text",
               'job': 'job from json',
               'work_size': 12,
               'collaborators': "5, 6",
               'start_date': '30-01-12',
               'is_finished': False
           }).json())  # POST запрос в котором id строка
print(post('http://localhost:5000/api/v2/jobs',
           json={
               'job_id': '20',
               'team_leader': 6,
               'job': 'job from json',
               'work_size': 12,
               'collaborators': "5, 6",
               'start_date': '30-01-12',
               'is_finished': False
           }).json())  # Правильный POST запрос

# Удаление 
print(delete('http://localhost:5000/api/v2/jobs/999').json())
# id = 999 нет в базе
print(delete('http://localhost:5000/api/v2/jobs/text').json())
# id = text не число
print(delete('http://localhost:5000/api/v2/jobs/20').json())

print(get('http://localhost:5000/api/v2/jobs').json())  # Все работы
