terraform {
  backend "s3" {
    endpoint = "https://nyc3.digitaloceanspaces.com"
    region   = "us-east-1"
    bucket   = "terraform-state-projeto-devops"
    key      = "terraform.tfstate"

    # IMPORTANTE: Adicione esta linha
    skip_requesting_account_id = true
    
    skip_credentials_validation = true
    skip_region_validation      = true
    skip_metadata_api_check     = true
    force_path_style            = true
  }
}
