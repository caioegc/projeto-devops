# Projeto DevOps - API de Tarefas com Docker

Este projeto consiste em uma API CRUD para gerenciamento de tarefas, utilizando Flask (Python) e PostgreSQL, containerizada com Docker e Docker Compose.

## 🚀 Tecnologias Utilizadas

- **Python 3.11** com Flask
- **PostgreSQL 15**
- **Docker** e **Docker Compose**
- **Multi-stage builds** com Alpine Linux

## 📋 Pré-requisitos

- Docker instalado
- Docker Compose instalado

## 🛠 Configuração e Execução

### 1. Clonar e acessar o projeto
```bash
git clone https://github.com/caioegc/projeto-devops.git
cd projeto-devops
```

### 2. Executar os containers

```powershell
docker compose up --build
```

### 3. Verificar se os serviços estão rodando

```powershell
docker compose ps
```

### 4. Acessar a aplicação

A API estará disponível em: http://localhost:5000


## 📊 Endpoints da API

### Health Check
```powershell
GET /
```
### Listar todas as tarefas
```powershell
GET /tasks
```

### Criar uma nova tarefa
```powershell
POST /tasks
Content-Type: application/json

{
  "title": "Minha tarefa",
  "description": "Descrição da tarefa"
}
```

### Obter uma tarefa específica
```powershell
GET /tasks/{id}
```

### Atualizar uma tarefa
```powershell
PUT /tasks/{id}
Content-Type: application/json

{
  "title": "Título atualizado",
  "completed": true
}
```

### Deletar uma tarefa
```powershell
DELETE /tasks/{id}
```

## 🧪 Testes com PowerShell


### Health Check
```powershell
Invoke-RestMethod -Uri "http://localhost:5000" -Method GET
```

### Criar uma tarefa
```powershell
Invoke-RestMethod -Uri "http://localhost:5000/tasks" -Method POST -Headers @{"Content-Type"="application/json"} -Body '{"title": "Estudar Docker", "description": "Completar atividade de DevOps"}'
```

### Listar todas as tarefas
```powershell
Invoke-RestMethod -Uri "http://localhost:5000/tasks" -Method GET
```

### Obter uma tarefa específica
```powershell
Invoke-RestMethod -Uri "http://localhost:5000/tasks/1" -Method GET
```

### Atualizar uma tarefa
```powershell
Invoke-RestMethod -Uri "http://localhost:5000/tasks/1" -Method PUT -Headers @{"Content-Type"="application/json"} -Body '{"completed": true}'
```

### Deletar uma tarefa
```powershell
Invoke-RestMethod -Uri "http://localhost:5000/tasks/1" -Method DELETE
```

Resultados esperados:
POST: Retorna a tarefa criada com ID

GET /tasks: Retorna lista de todas as tarefas

PUT: Retorna a tarefa atualizada

DELETE: Retorna mensagem de confirmação

## 🔒 Segurança
Usuário não-root: A aplicação roda com usuário dedicado myuser

Permissões limitadas: Usuário do banco app_user tem apenas permissões necessárias

Variáveis de ambiente: Configurações sensíveis isoladas

Rede isolada: Comunicação entre containers em rede customizada

## 🗄 Persistência de Dados
Os dados do PostgreSQL são persistidos em volume Docker:

projeto-devops_postgres_data

## 🌐 Variáveis de Ambiente
Aplicação
DATABASE_URL: URL de conexão com o PostgreSQL

FLASK_ENV: Ambiente de execução

Banco de Dados
POSTGRES_DB: tasks_db

POSTGRES_USER: app_user

POSTGRES_PASSWORD: app_password

## 🛑 Parar os containers

```powershell
docker compose down
```

## 📝 Estrutura do Projeto

projeto-devops/
├── app/
│   ├── app.py          # Aplicação Flask
│   └── .env            # Variáveis de ambiente
├── docker/
│   └── init.sql        # Script de inicialização do DB
├── .gitignore
├── docker-compose.yml  # Orquestração
├── Dockerfile          # Multi-stage build
├── README.md          # Este arquivo
└── requirements.txt    # Dependências Python

### 📞 Troubleshooting
## Verificar logs dos containers
```powershell
docker compose logs app
docker compose logs db
```
## Verificar se o banco está aceitando conexões
```powershell
docker compose exec db pg_isready
```
## Limpar tudo e recomeçar
```powershell
docker compose down -v
docker compose up --build
```