module "network" {
  source = "./modules/network"

  environment          = var.environment
  vpc_cidr             = var.vpc_cidr
  availability_zones   = var.availability_zones
  private_subnet_cidrs = var.private_subnet_cidrs
  public_subnet_cidrs  = var.public_subnet_cidrs
  global_tags          = var.global_tags
}

module "compute" {
  source = "./modules/compute"

  environment        = var.environment
  service_name       = var.service_name
  container_port     = var.container_port
  vpc_id             = module.network.vpc_id
  private_subnet_ids = module.network.private_subnet_ids
  public_subnet_ids  = module.network.public_subnet_ids
  global_tags        = var.global_tags
}

module "observability" {
  source = "./modules/observability"

  environment   = var.environment
  service_name  = var.service_name
  load_balancer = module.compute.load_balancer_arn_suffix
  global_tags   = var.global_tags
}
