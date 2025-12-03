import json
from flaskr import random_name


def test_index_route(app, client):
    res = client.get('/')
    assert res.status_code == 200
    html = res.get_data(as_text=True)

    # Check page contains expected structure
    assert "<h1" in html or "<h2" in html
    assert "flask" in html.lower()  # basic sanity check


def test_json_route(app, client):
    res = client.get('/json/')
    assert res.status_code == 200
    expected = {'hello': 'world'}
    assert expected == json.loads(res.get_data(as_text=True))


def test_hello_route(app, client):
    # default route
    res = client.get('/hello')
    assert res.status_code == 308
    res = client.get('/hello/')
    assert res.status_code == 200
    expected = "Hello Anonymous."
    assert expected in res.get_data(as_text=True)
    # custom name
    res = client.get('/hello/test')
    assert res.status_code == 200
    expected = "Hello test."
    assert expected in res.get_data(as_text=True)
    # random name
    res = client.get('/hello/random')
    assert res.status_code == 200


def test_primes_route(app, client):
    res = client.get('/primes/')
    assert res.status_code == 200
    
    res = client.get('/primes/5')
    assert res.status_code == 200
    
    # Get the response as text
    data = res.get_data(as_text=True)
    
    # Check for HTML structure and prime numbers
    assert '<!DOCTYPE html>' in data  # It's HTML
    assert '5' in data  # Limit is shown somewhere
    assert 'Prime' in data or 'prime' in data.lower()  # Something about primes
    
