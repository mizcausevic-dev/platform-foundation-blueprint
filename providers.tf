provider "aws" {
  region = var.aws_region
  access_key = var.offline_mode ? "mock_access_key" : null
  secret_key = var.offline_mode ? "mock_secret_key" : null
  skip_credentials_validation = var.offline_mode
  skip_requesting_account_id  = var.offline_mode
  skip_metadata_api_check     = var.offline_mode
  skip_region_validation      = var.offline_mode

  default_tags {
    tags = merge(var.global_tags, {
      blueprint = "platform-foundation"
      environment = var.environment
    })
  }
}
