import os
import psycopg2
from flask import Flask, request, jsonify
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

app = Flask(__name__)

# Configuração do banco de dados via variável de ambiente
DATABASE_URL = os.getenv('DATABASE_URL')

def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn

# Rota para health check
@app.route('/')
def hello():
    return jsonify({"message": "API de Tarefas funcionando!"})

# CREATE - Criar uma nova tarefa
@app.route('/tasks', methods=['POST'])
def create_task():
    try:
        data = request.get_json()
        title = data.get('title')
        description = data.get('description', '')

        if not title:
            return jsonify({"error": "Título é obrigatório"}), 400

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            'INSERT INTO tasks (title, description) VALUES (%s, %s) RETURNING id, title, description, completed',
            (title, description)
        )
        task = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()

        return jsonify({
            "id": task[0],
            "title": task[1],
            "description": task[2],
            "completed": task[3]
        }), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# READ - Listar todas as tarefas
@app.route('/tasks', methods=['GET'])
def get_tasks():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT id, title, description, completed FROM tasks ORDER BY created_at DESC')
        tasks = cur.fetchall()
        cur.close()
        conn.close()

        tasks_list = []
        for task in tasks:
            tasks_list.append({
                "id": task[0],
                "title": task[1],
                "description": task[2],
                "completed": task[3]
            })

        return jsonify(tasks_list)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# READ - Obter uma tarefa específica
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT id, title, description, completed FROM tasks WHERE id = %s', (task_id,))
        task = cur.fetchone()
        cur.close()
        conn.close()

        if task is None:
            return jsonify({"error": "Tarefa não encontrada"}), 404

        return jsonify({
            "id": task[0],
            "title": task[1],
            "description": task[2],
            "completed": task[3]
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# UPDATE - Atualizar uma tarefa
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    try:
        data = request.get_json()
        title = data.get('title')
        description = data.get('description')
        completed = data.get('completed')

        conn = get_db_connection()
        cur = conn.cursor()

        # Verifica se a tarefa existe
        cur.execute('SELECT id FROM tasks WHERE id = %s', (task_id,))
        if cur.fetchone() is None:
            cur.close()
            conn.close()
            return jsonify({"error": "Tarefa não encontrada"}), 404

        # Atualiza a tarefa
        cur.execute(
            'UPDATE tasks SET title = COALESCE(%s, title), description = COALESCE(%s, description), completed = COALESCE(%s, completed) WHERE id = %s RETURNING id, title, description, completed',
            (title, description, completed, task_id)
        )
        task = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()

        return jsonify({
            "id": task[0],
            "title": task[1],
            "description": task[2],
            "completed": task[3]
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# DELETE - Deletar uma tarefa
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        # Verifica se a tarefa existe
        cur.execute('SELECT id FROM tasks WHERE id = %s', (task_id,))
        if cur.fetchone() is None:
            cur.close()
            conn.close()
            return jsonify({"error": "Tarefa não encontrada"}), 404

        # Deleta a tarefa
        cur.execute('DELETE FROM tasks WHERE id = %s', (task_id,))
        conn.commit()
        cur.close()
        conn.close()

        return jsonify({"message": "Tarefa deletada com sucesso"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)