terraform {

  cloud {
    organization = "testhuseincomel"

    workspaces {
      name = "terraform-eks-aws"
    }
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.28.0"
    }
  }

  required_version = ">= 1.1.0"
}
