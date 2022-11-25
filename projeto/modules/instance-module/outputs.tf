output "instance_id" {
    value = aws_instance.main.id
    description = "Id of the instance"
}

output "instance_ami" {
    value = aws_instance.main.ami
    description = "AMI of the instance"
}

output "security_group_id" {
    value = aws_instance.main.vpc_security_group_ids
    description = "Id of the security group"
    
}


