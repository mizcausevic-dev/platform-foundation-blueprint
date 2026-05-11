# Platform Foundation Blueprint Architecture

This repo models a platform baseline in three clean lanes:

1. `network`
2. `compute`
3. `observability`

The intent is to show infrastructure thinking as a readable operating system design, not just a pile of provider resources.

## Network

The network module owns:

- the primary VPC
- public ingress subnets
- private service subnets
- internet gateway attachment

## Compute

The compute module owns:

- an ECS-style cluster baseline
- application load balancer
- target group health checks
- security group boundary for ingress

## Observability

The observability module owns:

- service log group
- a simple 5xx alarm tied to the ALB lane

## Why This Matters

The portfolio already has reliability, policy, governance, and escalation systems. This repo gives those control surfaces a plausible infrastructure floor:

- ingress exists
- workload placement exists
- alarms exist
- environments are explicit

That makes the rest of the platform work feel more grounded.
