environment          = "dev"
aws_region           = "us-east-1"
service_name         = "platform-runtime"
container_port       = 8080
vpc_cidr             = "10.40.0.0/16"
availability_zones   = ["us-east-1a", "us-east-1b"]
public_subnet_cidrs  = ["10.40.1.0/24", "10.40.2.0/24"]
private_subnet_cidrs = ["10.40.11.0/24", "10.40.12.0/24"]
global_tags = {
  owner  = "platform"
  system = "foundation"
}
