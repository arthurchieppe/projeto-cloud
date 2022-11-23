output "security_group_id" {
    value = aws_security_group.main.id
    description = "Id of the security group"
}

output "vpc_security_group" {
    value = aws_security_group.main.vpc_id
    description = "VPC of the security group"
}