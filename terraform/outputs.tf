output "droplet_ip" {
  description = "IP público do droplet criado"
  value       = digitalocean_droplet.app_server.ipv4_address
}