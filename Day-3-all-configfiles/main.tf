resource "aws_instance" "name" {
    ami = var.ami_id
    instance_type = var.instance_type
    subnet_id = var.subnet_id
    key_name = var.key_name
    associate_public_ip_address = true
    tags = {
        Name = "First Instance from Terraform"
    }
}