# VPC Creation
resource "aws_vpc" "testvpc" {
    cidr_block = "10.0.0.0/16"
    tags = {
      Name = "test"
    }
}

# Subnets Creation
resource "aws_subnet" "test-subnet"{
    vpc_id = aws_vpc.testvpc.id
    cidr_block = "10.0.0.0/24"
    availability_zone = "us-east-1a"
    tags = {
        Name = "test subnet"
    }
}

# IG
resource "aws_internet_gateway" "test-ig"{
    vpc_id = aws_vpc.testvpc.id
}

# Route table & Edit Routes
resource "aws_route_table" "test-rt"{
    vpc_id = aws_vpc.testvpc.id
    route = {
        cidr_block = "0.0.0.0/0"
        gateway_id = aws_internet_gateway.test-ig.id
    }
}

# subnet assocation
resource "aws_route_table_association" "test-rt_assocation"{
    subnet_id = aws_subnet.test-subnet.id
    route_table_id =  aws_route_table.test-rt.id
}

# SG Croup
resource "aws_security_group" "test-sg" {
    vpc_id = aws_vpc.testvpc.id

    #Write Egress (Outbound) and Ingress (Inbound) block
}


# NAT Creation
# EC2 creation


