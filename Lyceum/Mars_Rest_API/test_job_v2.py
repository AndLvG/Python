import pytest
from requests import get, post, delete, put

# Получение
def test_get1():
    resp = get('http://localhost:5000/api/v2/jobs/1').json()
    assert resp['job']['job'] == '"job": "deployment of residential modules 1 and 2"'
    assert resp['job']['team_leader'] == 6

def test_get2():
    resp = get('http://localhost:5000/api/v2/jobs/999').json()
    assert resp['message'] == 'Jobs 999 not found'

def test_get3():
    resp = get('http://localhost:5000/api/v2/users/aaa').json()
    assert resp['error'] == 'Not found'

# # Добавление
def test_post1():
    resp = post('http://localhost:5000/api/v2/jobs').json()
    assert resp['message'] == {"job_id": "Missing required parameter in the JSON body or the post body or the query string"}

def test_post2():
    resp = post(http://localhost:5000/api/v2/jobs',
           json={'title': 'Заголовок'}).json()
    assert resp['message'] == {"job_id": "Missing required parameter in the JSON body or the post body or the query string"}


# # Удаление 
def test_delete1():
    resp = delete('http://localhost:5000/api/v2/jobs/999').json()     
    assert resp['message'] == "Jobs 999 not found"

def test_delete2():
    resp = delete('http://localhost:5000/api/v2/jobs/text').json()  
    assert resp['error'] == 'Not found'


# Изменение
def test_put1():
    resp =put('http://localhost:5000/api/v2/jobs/999',
           json={
               'id': 999,
               'team_leader': 6,
               'job': 'job from json updated',
               'work_size': 12,
               'collaborators': "5, 6",
               'start_date': '30-01-12',
               'end_date': '30-01-20',
               'is_finished': True
           }).json()
    assert resp['error'] == 'Id <999> not found'
    

