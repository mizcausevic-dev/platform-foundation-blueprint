resource "aws_cloudwatch_log_group" "service" {
  name              = "/platform/${var.environment}/${var.service_name}"
  retention_in_days = 30

  tags = merge(var.global_tags, {
    lane = "observability"
  })
}

resource "aws_cloudwatch_metric_alarm" "alb_5xx" {
  alarm_name          = "${var.environment}-${var.service_name}-alb-5xx"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = 2
  metric_name         = "HTTPCode_Target_5XX_Count"
  namespace           = "AWS/ApplicationELB"
  period              = 60
  statistic           = "Sum"
  threshold           = 10
  alarm_description   = "Detects elevated 5xx pressure on the service ingress."

  dimensions = {
    LoadBalancer = var.load_balancer
  }

  tags = var.global_tags
}
