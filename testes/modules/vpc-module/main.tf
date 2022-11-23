module "aws_vpc" "vpc"{
  source  = "terraform-aws-modules/vpc/aws"
  version = "3.18.1"
  cidr_block = var.vpc_cidr_block

  tags = {
    Name = var.vpc_name
  }
}
