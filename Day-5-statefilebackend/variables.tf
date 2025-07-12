variable "ami_id" {
      description = "Instance ID"
      default = "ami-05ffe3c48a9991133"
}

variable "instance_type" {
      description = "Instance Type"
      default = "t2.micro"
}

variable "subnet_id" {
      description = "subnet id"
      default = "subnet-0c7f9446cc0f161c2"
}

variable "key_name" {
      description = "key pair"
      default = "aws-practice"
}

