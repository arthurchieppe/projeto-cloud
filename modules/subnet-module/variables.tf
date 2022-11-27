variable "subnet_name" {
  description = "Name of the subnet"
  type        = string
}

variable "subnet_cidr_block" {
  description = "CIDR block of the subnet"
  type        = string
  # default = "192.168.0.1/20"
}

variable "vpc_id" {
  description = "VPC ID"
  type        = string
}