import pytest
import json
from unittest.mock import Mock, patch
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@patch('app.psycopg2')
def test_hello_route(mock_psycopg2, client):
    """Testa a rota raiz"""
    response = client.get('/')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['message'] == 'API de Tarefas funcionando!'

@patch('app.psycopg2')
def test_create_task_success(mock_psycopg2, client):
    """Testa a criação bem-sucedida de uma tarefa"""
    # Mock do banco de dados
    mock_conn = Mock()
    mock_cur = Mock()
    mock_psycopg2.connect.return_value = mock_conn
    mock_conn.cursor.return_value = mock_cur
    mock_cur.fetchone.return_value = (1, 'Tarefa de Teste', 'Descrição de teste', False)
    
    task_data = {
        'title': 'Tarefa de Teste',
        'description': 'Descrição de teste'
    }
    
    response = client.post('/tasks', 
                         json=task_data,
                         content_type='application/json')
    
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['title'] == 'Tarefa de Teste'
    assert data['description'] == 'Descrição de teste'
    assert data['completed'] == False
    assert data['id'] == 1

@patch('app.psycopg2')
def test_create_task_without_title(mock_psycopg2, client):
    """Testa criação de tarefa sem título"""
    task_data = {
        'description': 'Descrição sem título'
    }
    
    response = client.post('/tasks', 
                         json=task_data,
                         content_type='application/json')
    
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'error' in data
    assert 'Título é obrigatório' in data['error']

@patch('app.psycopg2')
def test_get_tasks(mock_psycopg2, client):
    """Testa a listagem de tarefas"""
    # Mock do banco de dados
    mock_conn = Mock()
    mock_cur = Mock()
    mock_psycopg2.connect.return_value = mock_conn
    mock_conn.cursor.return_value = mock_cur
    mock_cur.fetchall.return_value = [
        (1, 'Tarefa 1', 'Descrição 1', False),
        (2, 'Tarefa 2', 'Descrição 2', True)
    ]
    
    response = client.get('/tasks')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)
    assert len(data) == 2
    assert data[0]['title'] == 'Tarefa 1'
    assert data[1]['title'] == 'Tarefa 2'

@patch('app.psycopg2')
def test_get_task_success(mock_psycopg2, client):
    """Testa busca por tarefa existente"""
    # Mock do banco de dados
    mock_conn = Mock()
    mock_cur = Mock()
    mock_psycopg2.connect.return_value = mock_conn
    mock_conn.cursor.return_value = mock_cur
    mock_cur.fetchone.return_value = (1, 'Tarefa Existente', 'Descrição', False)
    
    response = client.get('/tasks/1')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['id'] == 1
    assert data['title'] == 'Tarefa Existente'

@patch('app.psycopg2')
def test_get_nonexistent_task(mock_psycopg2, client):
    """Testa busca por tarefa inexistente"""
    # Mock do banco de dados
    mock_conn = Mock()
    mock_cur = Mock()
    mock_psycopg2.connect.return_value = mock_conn
    mock_conn.cursor.return_value = mock_cur
    mock_cur.fetchone.return_value = None
    
    response = client.get('/tasks/9999')
    assert response.status_code == 404
    data = json.loads(response.data)
    assert 'error' in data
    assert 'Tarefa não encontrada' in data['error']

@patch('app.psycopg2')
def test_update_task_success(mock_psycopg2, client):
    """Testa atualização de tarefa"""
    # Mock do banco de dados
    mock_conn = Mock()
    mock_cur = Mock()
    mock_psycopg2.connect.return_value = mock_conn
    mock_conn.cursor.return_value = mock_cur
    mock_cur.fetchone.side_effect = [
        (1,),  # Primeira chamada - verifica se existe
        (1, 'Tarefa Atualizada', 'Nova descrição', True)  # Segunda chamada - retorna atualizado
    ]
    
    update_data = {
        'title': 'Tarefa Atualizada',
        'description': 'Nova descrição',
        'completed': True
    }
    
    response = client.put('/tasks/1', json=update_data)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['title'] == 'Tarefa Atualizada'
    assert data['completed'] == True

@patch('app.psycopg2')
def test_update_nonexistent_task(mock_psycopg2, client):
    """Testa atualização de tarefa inexistente"""
    # Mock do banco de dados
    mock_conn = Mock()
    mock_cur = Mock()
    mock_psycopg2.connect.return_value = mock_conn
    mock_conn.cursor.return_value = mock_cur
    mock_cur.fetchone.return_value = None  # Tarefa não existe
    
    update_data = {'title': 'Título Atualizado'}
    
    response = client.put('/tasks/9999', json=update_data)
    assert response.status_code == 404
    data = json.loads(response.data)
    assert 'error' in data

@patch('app.psycopg2')
def test_delete_task_success(mock_psycopg2, client):
    """Testa exclusão de tarefa"""
    # Mock do banco de dados
    mock_conn = Mock()
    mock_cur = Mock()
    mock_psycopg2.connect.return_value = mock_conn
    mock_conn.cursor.return_value = mock_cur
    mock_cur.fetchone.return_value = (1,)  # Tarefa existe
    
    response = client.delete('/tasks/1')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'message' in data
    assert 'deletada com sucesso' in data['message']

@patch('app.psycopg2')
def test_delete_nonexistent_task(mock_psycopg2, client):
    """Testa exclusão de tarefa inexistente"""
    # Mock do banco de dados
    mock_conn = Mock()
    mock_cur = Mock()
    mock_psycopg2.connect.return_value = mock_conn
    mock_conn.cursor.return_value = mock_cur
    mock_cur.fetchone.return_value = None  # Tarefa não existe
    
    response = client.delete('/tasks/9999')
    assert response.status_code == 404
    data = json.loads(response.data)
    assert 'error' in data