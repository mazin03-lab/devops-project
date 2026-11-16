variable "aws_region" {
  description = "AWS region for deploying infrastructure"
  type        = string
  default     = "ap-southeast-2"
}

variable "project_name" {
  description = "Name of the DevOps Terraform project"
  type        = string
  default     = "devops-lab"
}

variable "vpc_cidr" {
  description = "CIDR range for the project VPC"
  type        = string
  default     = "10.20.0.0/16"
}
