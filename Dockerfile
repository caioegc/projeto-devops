# ==============================
# Etapa 1: Build (instala dependências)
# ==============================
FROM python:3.11-alpine AS builder

# Define diretório de trabalho
WORKDIR /app

# Instala dependências de compilação
RUN apk add --no-cache gcc musl-dev libpq-dev

# Copia arquivo de dependências
COPY requirements.txt .

# Instala dependências no diretório temporário /install
RUN pip install --prefix=/install -r requirements.txt


# ==============================
# Etapa 2: Runtime (imagem final leve)
# ==============================
FROM python:3.11-alpine

# Define diretório de trabalho
WORKDIR /app

# Copia dependências já instaladas do estágio builder
COPY --from=builder /install /usr/local

# Copia o código da aplicação
COPY app/ .

# Cria usuário não-root
RUN adduser -D myuser
USER myuser

# Expõe a porta da aplicação Flask
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "app.py"]
