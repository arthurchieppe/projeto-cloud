output "sg_id" {
    value = aws_security_group.main.id
    description = "Id of the security group"
}

output "vpc_of_sg" {
    value = aws_security_group.main.vpc_id
    description = "VPC of the security group"
}