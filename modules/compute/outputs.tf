output "cluster_name" {
  value = aws_ecs_cluster.this.name
}

output "load_balancer_dns_name" {
  value = aws_lb.this.dns_name
}

output "load_balancer_arn_suffix" {
  value = aws_lb.this.arn_suffix
}
