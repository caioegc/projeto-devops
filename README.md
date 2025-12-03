# Projeto DevOps Completo - API de Tarefas

## 🔗 Acesso Rápido
- **API Atual (Atividade 4)**: [http://159.89.43.79:5000](http://159.89.43.79:5000)
- **Repositório**: [github.com/caioegc/projeto-devops](https://github.com/caioegc/projeto-devops)
- **Pipeline CI/CD**: [GitHub Actions](https://github.com/caioegc/projeto-devops/actions)

## 🎯 Visão Geral
Projeto desenvolvido para a disciplina de DevOps, implementando uma API CRUD de tarefas com evolução através de 4 atividades práticas:
- **Atividade 1**: Aplicação Flask + PostgreSQL
- **Atividade 2**: Dockerização e Multi-container
- **Atividade 3**: CI/CD Pipeline com GitHub Actions
- **Atividade 4**: Infraestrutura como Código (IaC) com Terraform

---

## 📚 Atividades Desenvolvidas

### 🔹 **Atividade 1: Aplicação Base**
**Objetivo**: Desenvolver uma API CRUD para gerenciamento de tarefas usando Flask e PostgreSQL.

**Funcionalidades**:
- CRUD completo de tarefas
- Conexão com PostgreSQL
- Validação de dados

**Tecnologias**: Python, Flask, PostgreSQL, Psycopg2

---

### 🔹 **Atividade 2: Containerização e Docker Compose**
**Objetivo**: Dockerizar a aplicação e configurar ambiente multi-container.

**Implementação**:
- ✅ **Dockerfile multi-stage** com Alpine Linux
- ✅ **Docker Compose** com 2 serviços (app + PostgreSQL)
- ✅ **Rede customizada** para comunicação isolada
- ✅ **Volumes persistente** para dados do banco
- ✅ **Variáveis de ambiente** para configurações sensíveis
- ✅ **Usuário não-root** nos containers
- ✅ **Usuário dedicado no banco** (não root)

**Arquivos principais**:
- `Dockerfile` (multi-stage build)
- `docker-compose.yml`
- `.env.example`

**Comandos**:
```bash
# Desenvolvimento
docker compose up --build

# Produção
docker compose -f docker-compose.prod.yml up -d
```

---

### 🔹 **Atividade 3: CI/CD Pipeline com GitHub Actions**
**Objetivo**: Automatizar testes, build e deploy da aplicação.

**Pipeline Implementado**:
1. **Testes Unitários** - Execução automática dos testes Python
2. **Build da Imagem Docker** - Construção otimizada
3. **Push para Docker Hub** - Imagens taggeadas com `latest` e `commit-SHA`
4. **Deploy Automático** - Atualização no servidor via SSH

**Secrets Configurados**:
- `DOCKERHUB_USERNAME` e `DOCKERHUB_TOKEN`
- `SERVER_IP`, `SERVER_USER`, `SERVER_PASSWORD`

**Servidor Manual**:
- IP: `143.198.31.87:5000`
- Configuração inicial via SSH:
  ```bash
  git clone https://github.com/caioegc/projeto-devops.git /opt/projeto-devops
  cd /opt/projeto-devops
  # Configurar .env com variáveis de produção
  ```

**Status**: [![CI/CD Status](https://github.com/caioegc/projeto-devops/actions/workflows/cicd.yml/badge.svg)](https://github.com/caioegc/projeto-devops/actions)

---

### 🔹 **Atividade 4: Infraestrutura como Código (IaC)**
**Objetivo**: Automatizar a criação da infraestrutura com Terraform e integrar ao pipeline.

**Implementação**:

#### 📁 **Estrutura do Terraform** (`/terraform/`)
```
terraform/
├── main.tf           # Provider DigitalOcean + droplet com cloud-init
├── backend.tf        # Backend remoto (DigitalOcean Spaces)
├── variables.tf      # Variáveis de configuração
├── outputs.tf        # Output do IP público
└── terraform.tfvars  # Variáveis sensíveis (não versionado)
```

#### 🔧 **Recursos Provisionados**:
- **Droplet Ubuntu 22.04** (1vCPU, 1GB RAM)
- **Cloud-init** para instalação automática de Docker e Docker Compose
- **Chave SSH** injetada para acesso remoto
- **Tags** para organização (`app`, `terraform`, `devops`)

#### ☁️ **Backend Remoto**:
- **DigitalOcean Spaces** para armazenamento do estado do Terraform
- Configuração via secrets:
  - `SPACES_ACCESS_KEY_ID`
  - `SPACES_SECRET_ACCESS_KEY`

#### 🔄 **Pipeline Atualizado**:
Novo job `provision-infra` que:
1. Configura o Terraform com backend remoto
2. Aplica as mudanças (`terraform apply -auto-approve`)
3. Extrai o IP dinâmico do droplet
4. Passa o IP para o job de deploy via artifact

**Secrets Adicionais**:
- `DO_TOKEN`: Token da DigitalOcean
- `SPACES_ACCESS_KEY_ID` e `SPACES_SECRET_ACCESS_KEY`: Para backend remoto
- `SSH_PRIVATE_KEY`: Chave SSH para acesso ao novo droplet

**Servidor Automatizado**:
- IP Atual: `159.89.43.79:5000`
- Criado automaticamente a cada pipeline
- Docker e Docker Compose pré-instalados via `user_data`

---

## 🏗️ Arquitetura Final (Atividade 4)

```
GitHub Repository
    │
    ├── CI/CD Pipeline (GitHub Actions)
    │   ├── Testes Unitários
    │   ├── Provision Infra (Terraform) → Cria Droplet
    │   ├── Build & Push Docker Image
    │   └── Deploy Automático → Droplet Criado
    │
    └── Backend Remoto (DigitalOcean Spaces)
        └── Estado do Terraform
```

---

## 🚀 Como Executar

### 1. **Localmente (Desenvolvimento)**
```bash
git clone https://github.com/caioegc/projeto-devops.git
cd projeto-devops
docker compose up --build
# Acesse: http://localhost:5000
```

### 2. **Infraestrutura com Terraform**
```bash
cd terraform
terraform init
terraform plan
terraform apply -auto-approve
```

### 3. **Pipeline Automático**
- Push na branch `main` ativa automaticamente:
  1. Testes unitários
  2. Provisionamento do droplet
  3. Build da imagem Docker
  4. Deploy no servidor criado

---

## 🔗 Acessando a API

#### 🖥️ **Localmente**:
- URL: `http://localhost:5000`
- Porta: `5000`

#### 🌐 **Em Produção (Atividade 3 - Manual - atualmente esse localhost não está funcionando apenas o da atividade 4 funciona.)**:
- URL: `http://143.198.31.87:5000`
- Porta: `5000`

#### 🚀 **Em Produção (Atividade 4 - Automatizado)**:
- URL: `http://159.89.43.79:5000`
- Porta: `5000`

---

## 🧪 Testando a API

### Health Check:
```bash
curl http://159.89.43.79:5000/
```

### Listar tarefas:
```bash
curl http://159.89.43.79:5000/tasks
```

### Criar tarefa:
```bash
curl -X POST http://159.89.43.79:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Testar API", "description": "Verificar se está funcionando"}'
```

### Obter tarefa específica:
```bash
curl http://159.89.43.79:5000/tasks/1
```

### Atualizar tarefa:
```bash
curl -X PUT http://159.89.43.79:5000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"completed": true}'
```

### Deletar tarefa:
```bash
curl -X DELETE http://159.89.43.79:5000/tasks/1
```

---

## 📊 Resultados por Atividade

| Atividade | Status | Link/Evidência |
|-----------|--------|----------------|
| 1 - API Flask | ✅ Completa | [Código em `/app/`](https://github.com/caioegc/projeto-devops/tree/main/app) |
| 2 - Docker Compose | ✅ Completa | [`docker-compose.yml`](https://github.com/caioegc/projeto-devops/blob/main/docker-compose.yml) |
| 3 - CI/CD Pipeline | ✅ Completa | [GitHub Actions](https://github.com/caioegc/projeto-devops/actions) |
| 4 - IaC com Terraform | ✅ Completa | [Pasta `/terraform/`](https://github.com/caioegc/projeto-devops/tree/main/terraform) |

---

## 🔐 Segurança e Boas Práticas

✅ **Aplicação**:
- Usuário não-root nos containers
- Variáveis de ambiente para dados sensíveis
- Multi-stage builds com Alpine Linux

✅ **Banco de Dados**:
- Usuário dedicado (`app_user`) com permissões restritas
- Volume persistente para dados
- Rede isolada entre containers

✅ **Infraestrutura**:
- Estado do Terraform em backend remoto
- Chaves SSH injetadas automaticamente
- Cloud-init para configuração inicial

✅ **Pipeline**:
- Secrets do GitHub para credenciais
- Testes automatizados antes do deploy
- Imagens taggeadas com commit SHA

---

## 🛠️ Troubleshooting

### Problemas com SSH no droplet:
```bash
# Verificar chaves autorizadas
ssh -i ~/.ssh/id_ifal_do root@159.89.43.79 "cat ~/.ssh/authorized_keys"

# Verificar containers
ssh -i ~/.ssh/id_ifal_do root@159.89.43.79 "docker ps"
```

### Problemas no pipeline:
1. Verifique os logs do job `provision-infra`
2. Confirme os secrets no GitHub
3. Verifique o estado no DigitalOcean Spaces

---

## 📞 Contato

**Aluno**: Caio E. G. C.  
**Disciplina**: DevOps  
**Repositório**: [github.com/caioegc/projeto-devops](https://github.com/caioegc/projeto-devops)

---

*Projeto desenvolvido como parte das atividades práticas da disciplina de DevOps.*
