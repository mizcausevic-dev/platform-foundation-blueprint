# Platform Foundation Blueprint

Platform Foundation Blueprint is a Terraform infrastructure design for a policy-aware, multi-environment platform baseline. It frames networking, ingress, compute, and observability as one cohesive foundation instead of isolated cloud resources.

## Portfolio Takeaway

- Terraform-first infrastructure blueprint with environment overlays
- network, compute, and observability split into readable modules
- platform story that fits control rooms, governance, and reliability systems already in the portfolio
- real documentation and proof assets instead of a bare `main.tf`

## Overview

| Area | Details |
| --- | --- |
| IaC | Terraform |
| Cloud | AWS-oriented module structure |
| Focus | Multi-environment networking, ALB ingress, ECS-style compute, and observability alarms |
| Modules | `network`, `compute`, `observability` |
| Environments | `dev`, `prod` |
| Runtime Shape | Blueprint and module layout ready for `terraform init/plan` once Terraform is installed |

## What It Does

- establishes a VPC with public and private subnet lanes
- creates a load-balanced compute entry point
- wires a log group and 5xx alarm for operational visibility
- keeps env-specific settings in dedicated `tfvars` overlays

## Architecture

```mermaid
flowchart LR
  A["Environment tfvars"] --> B["Root Terraform composition"]
  B --> C["Network module"]
  B --> D["Compute module"]
  B --> E["Observability module"]
  C --> F["VPC and subnet lanes"]
  D --> G["ALB and ECS cluster"]
  E --> H["Logs and 5xx alarm"]
```

Additional detail lives in [docs/architecture.md](./docs/architecture.md).

## Module Layout

- `modules/network`
- `modules/compute`
- `modules/observability`
- `environments/dev.tfvars`
- `environments/prod.tfvars`

## Example Plan Flow

```powershell
cd platform-foundation-blueprint
terraform init
terraform plan -var-file="environments/dev.tfvars"
```

By default, this repo uses `offline_mode=true`, which allows local planning without real AWS credentials. That keeps the blueprint easy to inspect on a workstation before you wire it to a live account.

## Screenshots

### Hero
![Platform Foundation Blueprint hero](https://raw.githubusercontent.com/mizcausevic-dev/platform-foundation-blueprint/main/screenshots/01-hero.png)

### Module Lanes
![Platform Foundation Blueprint module lanes](https://raw.githubusercontent.com/mizcausevic-dev/platform-foundation-blueprint/main/screenshots/02-module-lanes.png)

### Environment Overlay
![Platform Foundation Blueprint environment overlay](https://raw.githubusercontent.com/mizcausevic-dev/platform-foundation-blueprint/main/screenshots/03-environments.png)

### Validation Proof
![Platform Foundation Blueprint proof](https://raw.githubusercontent.com/mizcausevic-dev/platform-foundation-blueprint/main/screenshots/04-proof.png)

## Local Run

For local proof and structure review:

```powershell
cd platform-foundation-blueprint
terraform init
terraform plan -var-file="environments/dev.tfvars"
```

For a real deployment-backed plan, turn off offline mode and use valid AWS credentials:

```powershell
terraform plan -var-file="environments/dev.tfvars" -var="offline_mode=false"
```

## Tech Stack

[![Terraform](https://img.shields.io/badge/Terraform-1.x-0f172a?style=for-the-badge&logo=terraform&logoColor=f8fafc)](https://developer.hashicorp.com/terraform)
[![AWS](https://img.shields.io/badge/AWS-blueprint-0f172a?style=for-the-badge&logo=amazonaws&logoColor=f8fafc)](https://aws.amazon.com/)

## Portfolio Links

- [Kinetic Gain](https://kineticgain.com/)
- [LinkedIn](https://www.linkedin.com/in/mirzacausevic)
- [GitHub](https://github.com/mizcausevic-dev)
- [Skills Page](https://mizcausevic.com/skills/)
