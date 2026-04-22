provider "aws" {
  region = "us-west-2"
}

resource "aws_s3_bucket" "secure_bucket" {
  bucket = "my-secure-bucket"
  acl    = "private"

  versioning {
    enabled = true
  }

  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }

  # Add lifecycle rule to expire objects after 30 days
  lifecycle_rule {
    enabled = true

    expiration {
      days = 30
    }
  }
}