provider "aws" {
  region = var.aws_region

  default_tags {
    tags = merge(var.global_tags, {
      blueprint = "platform-foundation"
      environment = var.environment
    })
  }
}
