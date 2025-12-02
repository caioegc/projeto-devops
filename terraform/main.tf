terraform {
  required_version = ">= 1.0"
  required_providers {
    digitalocean = {
      source  = "digitalocean/digitalocean"
      version = "~> 2.0"
    }
  }
}

provider "digitalocean" {
  token = var.do_token
}

# Chave SSH já cadastrada na DigitalOcean
data "digitalocean_ssh_key" "existing_key" {
  name = var.ssh_key_name
}

# Droplet (VPS) com cloud-init para instalar Docker e Docker Compose
resource "digitalocean_droplet" "app_server" {
  image    = "ubuntu-22-04-x64"
  name     = "app-server-iac"
  region   = var.region
  size     = var.droplet_size
  ssh_keys = [data.digitalocean_ssh_key.existing_key.id]

  # Script de inicialização (cloud-init)
  user_data = <<-EOF
              #cloud-config
              packages:
                - apt-transport-https
                - ca-certificates
                - curl
                - software-properties-common

              runcmd:
                # Instalar Docker
                - curl -fsSL https://get.docker.com -o get-docker.sh
                - sh get-docker.sh
                - usermod -aG docker ubuntu

                # Instalar Docker Compose
                - curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
                - chmod +x /usr/local/bin/docker-compose

                # Clonar seu repositório (opcional, mas útil)
                - cd /opt
                - git clone https://github.com/caioegc/projeto-devops.git || true

                # Criar .env manualmente depois (não versionado)
                - echo "O servidor está pronto com Docker e Docker Compose."
              EOF

  tags = ["app", "terraform", "devops"]
}