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
module "aws_security_group_ssh" {
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

instance = Template("""
module "aws_instance_${type}_${count}" {
    source  = "./modules/instance-module"

    instance_name = "TF ${type} Instance ${count}"
    instance_type = "${instance_type}"
    instance_ami        = "ami-08c40ec9ead489470"
    subnet_id     = module.aws_subnet.subnet_id
    vpc_security_group_ids = [module.aws_security_group_ssh.security_group_id]
}
"""
)

iam_user = Template("""
module "aws_iam_user" {
    source  = "./modules/aws_iam_user"

    username = "${name}"

}
"""
)




