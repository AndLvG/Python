import pytest
from requests import get, post, delete, put

# Получение
def test_get1():
    resp = get('http://localhost:5000/api/v2/users/1').json()
    assert resp['user']['name'] == 'Ridley'
    assert resp['user']['position'] == 'captain'

def test_get2():
    resp = get('http://localhost:5000/api/v2/users/999').json()
    assert resp['message'] == 'User 999 not found'

def test_get3():
    resp = get('http://localhost:5000/api/v2/users/aaa').json()
    assert resp['error'] == 'Not found'

# # Добавление
def test_post1():
    resp = post('http://localhost:5000/api/v2/users').json()
    print(resp)
    assert resp['message'] == {'user_id': 'Missing required parameter in the JSON body or the post body or the query string'}

def test_post2():
    resp = post('http://localhost:5000/api/v2/users', json={'title': 'Заголовок'}).json()
    assert resp['message'] == {'user_id': 'Missing required parameter in the JSON body or the post body or the query string'}

# # Удаление 
def test_delete1():
    resp = delete('http://localhost:5000/api/v2/users/text').json()     
    assert resp['error'] == 'Id <999> not found'

def test_delete2():
    resp = delete('http://localhost:5000/api/v2/users/text').json()  
    assert resp['error'] == 'Not found'


# Изменение
def test_put1():
    resp =put('http://localhost:5000/api/v2/users/999',
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
           }).json()
    assert resp['error'] == 'Id <999> not found'
    

def test_put2():
    resp = put('http://localhost:5000/api/v2/users/20',
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
           }).json()
    assert resp['error'] == 'Id not int()'


# test_put1()
# test_put2()