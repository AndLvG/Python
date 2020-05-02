import pytest
from requests import get, post, delete, put


# Изменение работы
def test_put1():
    resp = put('http://localhost:5000/api/jobs',
           json={
               'id': 999,
               'team_leader': 6,
               'job': 'job from json updated',
               'work_size': 12,
               'collaborators': "5, 6",
               'start_date': '30-01-12',
               'end_date': '30-01-20',
               'is_finished': True
           }) 
    assert resp.status_code == 200
    resp_body = resp.json()
    assert resp_body['error'] == 'Id <999> not found'
    

def test_put2():
    resp = put('http://localhost:5000/api/jobs',
           json={
               'id': 'ttt',
               'team_leader': 6,
               'job': 'job from json updated',
               'work_size': 12,
               'collaborators': "5, 6",
               'start_date': '30-01-12',
               'end_date': '30-01-20',
               'is_finished': True
           })
    print()
    assert resp.status_code == 200
    resp_body = resp.json()
    assert resp_body['error'] == 'Id not int()'


# test_put1()
# test_put2()