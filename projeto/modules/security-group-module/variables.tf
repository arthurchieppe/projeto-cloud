variable "security_group_name" {
  type        = string
  description = "Security Group Name"
}

variable "vpc_id" {
  type        = string
  description = "VPC ID"
}

variable "vpc_cidr_blocks" {
  type        = string
  description = "List of CIDR blocks to allow ingress traffic"
}