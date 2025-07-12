terraform {
  backend "s3" {
    bucket         = "pankaj-terraform-statelock"
    key            = "terraform.tfstate"
    region         = "us-east-1"
    # dynamodb_table = "your-dynamodb-table"
    use_lockfile   = true
  }
}
