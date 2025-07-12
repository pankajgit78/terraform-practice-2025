output "public_ip"{
    value = aws_instance.name.public_ip
    description = "output public ip"
}

output "vpc_id"{
    value = aws_instance.name.id
    description = "output vpc ip"
}