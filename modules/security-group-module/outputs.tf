output "security_group_id" {
    value = aws_security_group.main.id
    description = "Id of the security group"
}

output "vpc_security_group" {
    value = aws_security_group.main.vpc_id
    description = "VPC of the security group"
}

output "security_group_name" {
    value = aws_security_group.main.name
    description = "Name of the security group"
}

output "security_group_description" {
    value = aws_security_group.main.description
    description = "Description of the security group"
}