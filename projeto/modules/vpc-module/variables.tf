variable "vpc_name" {
  type        = string
  description = "VPC Name"
}

variable "vpc_cidr_block" {
  type        = string
  description = "VPC CIDR Block"
  # default = "192.168.0.0/20"
}