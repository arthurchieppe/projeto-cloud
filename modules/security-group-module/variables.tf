variable "security_group_name" {
  type        = string
  description = "Security Group Name"
}

variable "vpc_id" {
  type        = string
  description = "VPC ID"
}

# Ingress:
variable "ingress_descritpion" {
  type        = string
  description = "Ingress Description"
  default = "Default ingress description"
}

variable "ingress_from_port" {
  type        = number
  description = "Ingress From Port"
  default = 22
}

variable "ingress_to_port" {
  type        = number
  description = "Ingress To Port"
  default = 22
}

variable "ingress_protocol" {
  type        = string
  description = "Ingress Protocol"
  default = "tcp"
}

variable "ingress_cidr_blocks" {
  type        = string
  description = "Ingress CIDR Blocks"
}

# Egress:

variable "egress_descritpion" {
  type        = string
  description = "Egress Description"
  default = "Default egress description"
}

variable "egress_from_port" {
  type        = number
  description = "Egress From Port"
}

variable "egress_to_port" {
  type        = number
  description = "Egress To Port"
}

variable "egress_protocol" {
  type        = string
  description = "Egress Protocol"
}

variable "egress_cidr_blocks" {
  type        = string
  description = "Egress CIDR Blocks"
}