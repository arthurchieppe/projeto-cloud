terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region = "us-east-1"
}

module "aws_vpc" {
  source  = "./modules/vpc-module"

  vpc_name       = "TF VPC"
  vpc_cidr_block = "192.168.0.0/24"
}

module "aws_subnet" {
  source  = "./modules/subnet-module"

  subnet_name       = "TF Subnet"
  subnet_cidr_block = "192.168.1.0/24"
}

module "security_group"{
  source  = "./modules/security-group-module"

  security_group_name = "TF Security Group"
  vpc_id              = module.aws_vpc.main.id
}


resource "aws_instance" "app_server" {
  ami                    = "ami-0ee23bfc74a881de5"
  instance_type          = "t2.micro"
  vpc_security_group_ids = ["sg-064bc54f9436797d6"]
  subnet_id              = "subnet-005c117c6bc330ea6"

  tags = {
    Name = var.instance_name
  }
}

variable "instance_name" {
  description = "Value of the Name tag for the EC2 instance"
  type        = string
  default     = "ExampleAppServerInstance"
}
