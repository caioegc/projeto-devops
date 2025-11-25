-- Cria o usuário da aplicação se não existir
DO $$ 
BEGIN 
  IF NOT EXISTS (SELECT FROM pg_catalog.pg_roles WHERE rolname = 'app_user') THEN
    CREATE USER app_user WITH PASSWORD 'app_password';
  END IF;
END $$;

-- Concede permissões básicas
GRANT CONNECT ON DATABASE tasks_db TO app_user;
GRANT USAGE ON SCHEMA public TO app_user;

-- Cria a tabela de tasks
CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    completed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Garante permissões ESPECÍFICAS na tabela tasks
GRANT SELECT, INSERT, UPDATE, DELETE ON tasks TO app_user;

-- Garante permissões na sequência do ID autoincrement
GRANT USAGE, SELECT ON SEQUENCE tasks_id_seq TO app_user;

-- Permissões para tabelas futuras (opcional, mas mantém a flexibilidade)
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO app_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT USAGE, SELECT ON SEQUENCES TO app_user;