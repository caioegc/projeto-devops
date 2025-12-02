variable "do_token" {
  description = "Token de API da DigitalOcean"
  type        = string
  sensitive   = true
}

variable "ssh_key_name" {
  description = "Nome da chave SSH cadastrada na DigitalOcean"
  type        = string
  default     = "ifal-chave"

}

variable "region" {
  description = "Região do droplet"
  type        = string
  default     = "nyc3"
}

variable "droplet_size" {
  description = "Tamanho do droplet"
  type        = string
  default     = "s-1vcpu-1gb"
}