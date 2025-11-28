# Projeto DevOps - API de Tarefas com Docker a

Este projeto consiste em uma API CRUD para gerenciamento de tarefas, utilizando Flask (Python) e PostgreSQL, containerizada com Docker e Docker Compose.


## ⚙️ Tecnologias Utilizadas

### 🐳 Infraestrutura & DevOps

 Tecnologia                                                                                                              | Descrição                                                                            |
| :---------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------- |
| ![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge\&logo=docker\&logoColor=white)                 | Containerização da aplicação e banco de dados para ambiente isolado e consistente.   |
| ![Docker Compose](https://img.shields.io/badge/Docker_Compose-2496ED?style=for-the-badge\&logo=docker\&logoColor=white) | Orquestração de multi-containers para gerenciar aplicação e banco simultaneamente.   |
| ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge\&logo=postgresql\&logoColor=white)     | Banco de dados relacional para persistência dos dados com usuário dedicado e seguro. |

---

### 🐍 Back-end & API

|Tecnologia                                                                                                      | Descrição                                                                           |
| :-------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------- |
| ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)         | Linguagem principal usada para implementar a API RESTful e lógica de negócio.       |
| ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge\&logo=flask\&logoColor=white)            | Framework web leve para criação da API com endpoints CRUD e tratamento de requests. |
| ![Psycopg2](https://img.shields.io/badge/Psycopg2-4169E1?style=for-the-badge\&logo=postgresql\&logoColor=white) | Driver PostgreSQL para Python, permitindo conexão segura com o banco de dados.      |

---

### 🔒 Segurança & Boas Práticas

 Tecnologia                                                                                                                     | Descrição                                                                       |
| :----------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------ |
| ![Multi-stage Build](https://img.shields.io/badge/Multi--stage_Build-2496ED?style=for-the-badge\&logo=docker\&logoColor=white) | Builds otimizados com imagens Alpine Linux para tamanho reduzido e segurança.   |
| ![Environment Variables](https://img.shields.io/badge/Environment_Variables-4A90E2?style=for-the-badge)                        | Configurações sensíveis isoladas em variáveis de ambiente para maior segurança. |
| ![Non-root User](https://img.shields.io/badge/Non--root_User-FF6B6B?style=for-the-badge)                                       | Aplicação executa com usuário dedicado, seguindo princípio do menor privilégio. |


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
--- 

### Testar:
Testar listagem de tarefas (para ver tudo funcionando)
Usando curl:
```bash
curl http://localhost:5000/tasks
```

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

### 4. Acessar a aplicação
A aplicação também está rodando no servidor DigitalOcean, disponível publicamente no IP do droplet.

- Localmente (Docker): http://localhost:5000  
- No servidor DigitalOcean: http://143.198.31.87:5000

## CI/CD Pipeline

[![CI/CD Status](https://github.com/caioegc/projeto-devops/actions/workflows/cicd.yml/badge.svg)](https://github.com/caioegc/projeto-devops/actions)

### Fluxo do Pipeline:
1. **Testes**: A cada push na branch main, os testes unitários são executados
2. **Build**: Se os testes passarem, uma nova imagem Docker é construída
3. **Push**: A imagem é enviada para o Docker Hub com tags `latest` e `commit-SHA`
4. **Deploy**: A aplicação é automaticamente atualizada no servidor de produção

### Secrets Necessários:
- `DOCKERHUB_USERNAME`: Usuário do Docker Hub
- `DOCKERHUB_TOKEN`: Token de acesso do Docker Hub  
- `SERVER_IP`: IP do servidor de produção
- `SERVER_USER`: Usuário SSH do servidor
- `SERVER_PASSWORD`: Senha do servidor

### Configuração Manual no Servidor:
```bash
git clone <repo-url> /opt/projeto-devops
cd /opt/projeto-devops
```
### Configuração Manual no Servidor:
```bash
git clone https://github.com/caioegc/projeto-devops.git /opt/projeto-devops
cd /opt/projeto-devops
```
# Criar arquivo .env com variáveis de produção
cat > .env << EOF
DATABASE_URL=postgresql://app_user:app_password@db:5432/tasks_db
FLASK_ENV=production
EOF
