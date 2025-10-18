# Imagem base mais compatível
FROM python:3.11-slim

WORKDIR /app

# Instala dependências do sistema necessárias
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia e instala dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY app/ .

# Cria usuário não-root por segurança
RUN useradd -m myuser
USER myuser

# Expõe a porta da aplicação
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "app.py"]