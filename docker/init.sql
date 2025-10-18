DO $$ 
BEGIN 
  IF NOT EXISTS (SELECT FROM pg_catalog.pg_roles WHERE rolname = 'app_user') THEN
    CREATE USER app_user WITH PASSWORD 'app_password';
  END IF;
END $$;

-- Concede permissões limitadas
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

-- Garante permissões na tabela criada
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO app_user;
GRANT USAGE ON ALL SEQUENCES IN SCHEMA public TO app_user;