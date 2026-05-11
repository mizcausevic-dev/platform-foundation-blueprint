output "vpc_id" {
  description = "Primary VPC identifier."
  value       = module.network.vpc_id
}

output "alb_dns_name" {
  description = "Application load balancer DNS name."
  value       = module.compute.load_balancer_dns_name
}

output "cluster_name" {
  description = "Primary ECS cluster name."
  value       = module.compute.cluster_name
}

output "log_group_name" {
  description = "CloudWatch log group for the service."
  value       = module.observability.log_group_name
}
