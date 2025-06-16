import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'app')))
from app import app

def test_home():
    response = app.test_client().get('/')
    assert response.status_code == 200

def test_get_characters():
    response = app.test_client().get('/characters')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_get_character_by_name():
    response = app.test_client().get('/characters/Iron Man')
    assert response.status_code == 200
    assert response.json['real_name'] == 'Tony Stark'

def test_get_character_not_found():
    response = app.test_client().get('/characters/Batman')
    assert response.status_code == 404