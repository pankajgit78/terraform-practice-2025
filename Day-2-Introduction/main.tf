resource "aws_instance" "name" {
    ami = "ami-05ffe3c48a9991133"
    instance_type = "t2.micro"
    subnet_id = "subnet-0c7f9446cc0f161c2"
    key_name = "aws-practice"
    tags = {
        Name = "First Instance from Terraform"
    }
}

