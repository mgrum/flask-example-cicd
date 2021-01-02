import json
from flaskr import app as flaskr_app


def test_index_route(app, client):
    res = client.get('/')
    assert res.status_code == 200
    expected = '<h1>' + flaskr_app.hello_message + '</h1>'
    assert expected in res.get_data(as_text=True)

def test_json_route(app, client):
    res = client.get('/json/')
    assert res.status_code == 200
    expected = {'hello': 'world'}
    assert expected == json.loads(res.get_data(as_text=True))
    
def test_hello_route(app, client):
    res = client.get('/hello')
    assert res.status_code == 308
    res = client.get('/hello/')
    assert res.status_code == 200
    expected = "Hello Anonymous."
    assert expected == res.get_data(as_text=True)
    res = client.get('/hello/test')
    assert res.status_code == 200
    expected = "Hello test."
    assert expected == res.get_data(as_text=True)
    
def test_primes_route(app, client):
    res = client.get('/primes/')
    assert res.status_code == 200
    res = client.get('/primes/5')
    assert res.status_code == 200
    expected = '[2, 3, 5, 7, 11]'
    assert expected in res.get_data(as_text=True)