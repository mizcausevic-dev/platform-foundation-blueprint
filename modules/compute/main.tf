resource "aws_ecs_cluster" "this" {
  name = "${var.environment}-${var.service_name}"

  tags = merge(var.global_tags, {
    lane = "compute"
  })
}

resource "aws_security_group" "alb" {
  name        = "${var.environment}-${var.service_name}-alb"
  description = "ALB security group"
  vpc_id      = var.vpc_id

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = var.global_tags
}

resource "aws_lb" "this" {
  name               = substr("${var.environment}-${var.service_name}", 0, 32)
  load_balancer_type = "application"
  internal           = false
  security_groups    = [aws_security_group.alb.id]
  subnets            = var.public_subnet_ids

  tags = merge(var.global_tags, {
    lane = "compute"
  })
}

resource "aws_lb_target_group" "this" {
  name        = substr("${var.environment}-${var.service_name}-tg", 0, 32)
  port        = var.container_port
  protocol    = "HTTP"
  target_type = "ip"
  vpc_id      = var.vpc_id

  health_check {
    path = "/health"
  }

  tags = var.global_tags
}

resource "aws_lb_listener" "http" {
  load_balancer_arn = aws_lb.this.arn
  port              = 80
  protocol          = "HTTP"

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.this.arn
  }
}
