# EKS Cluster Setup with Terraform

This guide provides step-by-step instructions for setting up an Amazon EKS (Elastic Kubernetes Service) cluster using Terraform, including configuring a VPC, subnets, and security settings.

## Prerequisites

- AWS Account with Administrator access.
- IAM Role with `AdministratorAccess` policy attached.
- Amazon EC2 instance running Amazon Linux 2.
- Run everything from root user **sudo su**


## Step 1: Set Up EC2 Instance

1. Launch an EC2 instance with Amazon Linux 2 and attach an IAM role with AdministratorAccess permissions.
2. SSH into the instance and update packages with `sudo yum update -y`.
3. Install Terraform by downloading and unzipping the binary, then moving it to `/usr/local/bin/` and verifying with `terraform -v`.

```bash
yum update -y
wget https://releases.hashicorp.com/terraform/1.5.5/terraform_1.5.5_linux_amd64.zip
unzip terraform_1.5.5_linux_amd64.zip
sudo rm /usr/local/bin/terraform
sudo mv terraform /usr/local/bin/
terraform -v
```

## Step 2: Set Up Terraform Files

1. Create a project directory for your EKS configuration files with `mkdir eks && cd eks`.
2. Create the necessary Terraform files in the `eks` directory: `main.tf`, `providers.tf`, `variables.tf`, `eks.tf`, and `vpc.tf`.


## Step 3: Configure Terraform Files

### providers.tf

```hcl
provider "aws" {
  default_tags {
    tags = local.tags
  }
}

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 4.67.0"
    }
  }

  required_version = ">= 1.4.2"
}
```

Configure your AWS provider in `providers.tf` with the region set to your desired AWS region.

### vpc.tf

In `vpc.tf`, configure the VPC, availability zones, and subnets required for EKS. This setup includes both public and private subnets with NAT gateway and Internet Gateway configurations for traffic routing. 

Define the availability zones and create private and public subnets using CIDR ranges. Set the VPC configuration options, such as enabling the NAT gateway, DNS hostnames, Internet Gateway, and default network ACL, route tables, and security groups. Tags are added to the subnets for integration with Kubernetes, designating roles for ELB and internal ELB on public and private subnets.

```hcl
data "aws_availability_zones" "available" {
  state = "available"
}

locals {
  # Create subnets for each Availability Zone
  azs            = slice(data.aws_availability_zones.available.names, 0, min(length(data.aws_availability_zones.available.names), 3))
  private_subnets = [for k, v in local.azs : cidrsubnet(var.vpc_cidr, 3, k + 3)]
  public_subnets  = [for k, v in local.azs : cidrsubnet(var.vpc_cidr, 3, k)]
}

module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "~> 5.1"

  name = var.cluster_name
  cidr = var.vpc_cidr

  # Define Availability Zones and subnets
  azs                   = local.azs
  public_subnets        = local.public_subnets
  private_subnets       = local.private_subnets
  public_subnet_suffix  = "SubnetPublic"
  private_subnet_suffix = "SubnetPrivate"

  # VPC configuration options
  enable_nat_gateway    = true
  create_igw            = true
  enable_dns_hostnames  = true
  single_nat_gateway    = true

  # Enable management of default resources for easier tagging and customization
  manage_default_network_acl    = true
  default_network_acl_tags      = { Name = "${var.cluster_name}-default" }
  manage_default_route_table    = true
  default_route_table_tags      = { Name = "${var.cluster_name}-default" }
  manage_default_security_group = true
  default_security_group_tags   = { Name = "${var.cluster_name}-default" }

  # Tags for subnets
  public_subnet_tags = merge(local.tags, {
    "kubernetes.io/role/elb" = "1"
  })
  private_subnet_tags = merge(local.tags, {
    "karpenter.sh/discovery"          = var.cluster_name
    "kubernetes.io/role/internal-elb" = "1"
  })

  tags = local.tags
}

```
### eks.tf

Define your EKS cluster and managed node groups in `eks.tf`. Set up cluster properties such as name, version, and endpoint accessibility. Use the VPC’s private subnets and configure managed node groups with desired instance types, minimum and maximum sizes, labels, and tags.
```hcl
module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "~> 20.0"

  cluster_name                             = var.cluster_name
  cluster_version                          = var.cluster_version
  cluster_endpoint_public_access           = true
  enable_cluster_creator_admin_permissions = true

  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.vpc.private_subnets

  eks_managed_node_groups = {
    default = {
      instance_types           = ["m5.large"]
      min_size                 = 3
      max_size                 = 6
      desired_size             = 3
      labels                   = { workshop-default = "yes" }
    }
  }

  tags = merge(local.tags, {
    "karpenter.sh/discovery" = var.cluster_name
  })
}

```
### main.tf
```hcl
locals {
  tags = {
    created-by = "eks-workshop"
    env        = var.cluster_name
  }
}
```
Define project-wide tags in `main.tf` for consistent identification, including tags for created-by and environment variables referencing the cluster name.

### variables.tf

Define the variables used in your configuration in `variables.tf`. These variables include `cluster_name`, `cluster_version`, `ami_release_version`, and `vpc_cidr`, with descriptions and default values for each.
```hcl
variable "cluster_name" {
  description = "Name of the EKS cluster"
  type        = string
  default     = "eks-workshop"
}

variable "cluster_version" {
  description = "EKS cluster version."
  type        = string
  default     = "1.30"
}

variable "ami_release_version" {
  description = "Default EKS AMI release version for node groups"
  type        = string
  default     = "1.30.0-20240625"
}

variable "vpc_cidr" {
  description = "Defines the CIDR block used on Amazon VPC created for Amazon EKS."
  type        = string
  default     = "10.42.0.0/16"
}
```

## Step 4: Initialize and Deploy EKS Cluster

1. Export the desired cluster name as an environment variable: `export EKS_CLUSTER_NAME=dev`.
2. Initialize Terraform in the `eks` directory with `terraform init`.
3. Review the planned changes by running `terraform plan`.
4. Apply the configuration to create the EKS cluster using `terraform apply -var="cluster_name=$EKS_CLUSTER_NAME" -auto-approve`.

Your EKS cluster is now configured and deployed, complete with a VPC, subnets, and security settings. Verify the cluster status and node groups using the AWS Console or `kubectl`.

- Download `kubectl` with `curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.30.4/2024-09-11/bin/linux/amd64/kubectl`.
- Move `kubectl` to `/usr/local/bin/` with `cp kubectl /usr/local/bin/`.

## Step 5: Verify AWS IAM role and EKS configuration:

   - Use `aws sts get-caller-identity` to confirm your IAM role.
   - Configure access to the EKS cluster with `aws eks update-kubeconfig --region us-west-1 --name dev`.
   - Install Helm, a package manager for Kubernetes:
   - Download the Helm installation script with `curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3`.
   - Set permissions and run the script with `chmod 700 get_helm.sh` and `./get_helm.sh`.

