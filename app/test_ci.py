import pytest
import json
from app import app

@pytest.fixture
def client():
    """Fixture para testes CI"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_ci_basic_routes(client):
    """Testes básicos que devem passar sempre no CI"""
    
    # Teste da rota raiz
    response = client.get('/')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['message'] == 'API de Tarefas funcionando!'
    
    # Teste de validação (sem título)
    task_data = {'description': 'Sem título'}
    response = client.post('/tasks', json=task_data)
    assert response.status_code == 400
    assert 'error' in json.loads(response.data)

def test_ci_app_import():
    """Testa se o app importa corretamente"""
    from app import app
    assert app is not None
    assert hasattr(app, 'route')