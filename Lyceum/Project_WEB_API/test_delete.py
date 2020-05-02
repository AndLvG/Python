import pytest
from requests import get, post, delete, put

# Удаление работы
def test_delete1():
    resp = delete('http://localhost:5000/api/jobs/999')     
    assert resp.status_code == 200
    resp_body = resp.json()
    assert resp_body['error'] == 'Id <999> not found'
    

def test_delete2():
    resp = delete('http://localhost:5000/api/jobs/text')   
    assert resp.status_code == 404
    resp_body = resp.json()
    assert resp_body['error'] == 'Not found'

# test_delete1()
# test_delete2()