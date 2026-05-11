variable "environment" {
  type = string
}

variable "service_name" {
  type = string
}

variable "container_port" {
  type = number
}

variable "vpc_id" {
  type = string
}

variable "private_subnet_ids" {
  type = list(string)
}

variable "public_subnet_ids" {
  type = list(string)
}

variable "global_tags" {
  type = map(string)
}
