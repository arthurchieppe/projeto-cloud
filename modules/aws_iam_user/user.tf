resource "aws_iam_user" "main" {
  name = var.username

  tags = {
    Name = var.username
  }
}