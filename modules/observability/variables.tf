variable "environment" {
  type = string
}

variable "service_name" {
  type = string
}

variable "load_balancer" {
  type = string
}

variable "global_tags" {
  type = map(string)
}
