resource "aws_instance" "main" {
  ami                    = var.instance_ami             #"ami-08c40ec9ead489470"
  instance_type          = var.instance_type            # "t2.micro"
  vpc_security_group_ids = var.vpc_security_group_ids   # ["sg-064bc54f9436797d6"]
  subnet_id              = var.subnet_id                # "subnet-005c117c6bc330ea6"

  tags = {
    Name = var.instance_name
  }
}