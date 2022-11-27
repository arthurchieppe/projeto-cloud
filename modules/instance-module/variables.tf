variable "instance_name" {
    description = "Value of the Name tag for the EC2 instance"
    type        = string
}

variable "instance_ami" {
    description = "AMI ID of the EC2 instance"
    type        = string
    default     = "ami-08c40ec9ead489470"  # Ubuntu 18.04 LTS
}

variable "instance_type" {
    description = "Type of the EC2 instance"
    type        = string
    default     = "t2.micro"
}

variable "vpc_security_group_ids" {
    description = "Security Group ID of the EC2 instance"
    type        = list(string)          # Only SSH access
}

variable "subnet_id" {
    description = "Subnet ID of the EC2 instance"
    type        = string
}