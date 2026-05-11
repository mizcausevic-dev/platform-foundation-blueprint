variable "environment" {
  type        = string
  description = "Deployment environment name."
}

variable "aws_region" {
  type        = string
  description = "AWS region for the foundation."
}

variable "global_tags" {
  type        = map(string)
  description = "Shared tags across all modules."
}

variable "vpc_cidr" {
  type        = string
  description = "Primary CIDR block for the platform VPC."
}

variable "availability_zones" {
  type        = list(string)
  description = "Availability zones used by the platform."
}

variable "private_subnet_cidrs" {
  type        = list(string)
  description = "Private subnet ranges."
}

variable "public_subnet_cidrs" {
  type        = list(string)
  description = "Public subnet ranges."
}

variable "service_name" {
  type        = string
  description = "Primary service family this foundation supports."
}

variable "container_port" {
  type        = number
  description = "Container port for the application load balancer target."
}
