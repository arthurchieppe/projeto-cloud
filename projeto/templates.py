from string import Template

terraform_config = """
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}
"""


aws_provider = """
provider "aws" {
    region = "us-east-1"
}
"""

vpc_subnet = Template("""
module "aws_vpc" {
  source  = "./modules/vpc-module"

  vpc_name       = "Terrafom VPC"
  vpc_cidr_block = "192.168.0.0/20"
}

module "aws_subnet" {
  source  = "./modules/subnet-module"

  subnet_name       = "TF Subnet"
  subnet_cidr_block = module.aws_vpc.cidr_block
  vpc_id            = module.aws_vpc.vpc_id
}
""")

security_group_only_ssh = Template("""
module "aws_security_group" {
    source  = "./modules/security-group-module"

    security_group_name = "SSH Only"
    vpc_id              = module.aws_vpc.vpc_id
    ingress_cidr_blocks = "0.0.0.0/0"
    ingress_protocol    = "tcp"
    ingress_from_port   = 22
    ingress_to_port     = 22

    egress_cidr_blocks  = "0.0.0.0/0"
    egress_protocol     = "-1"
    egress_from_port    = 0
    egress_to_port      = 0
}
""")




