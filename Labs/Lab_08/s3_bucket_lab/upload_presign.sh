#!/bin/bash

# upload_presign.sh
# Usage: ./upload_presign.sh local_file bucket_name expiration_seconds

LOCAL_FILE=$1
BUCKET_NAME=$2
EXPIRATION=$3

# Check if all arguments are provided
if [ $# -ne 3 ]; then
    echo "Usage: $0 local_file bucket_name expiration_seconds"
    exit 1
fi

# Upload the file to S3
aws s3 cp "$LOCAL_FILE" "s3://$BUCKET_NAME/"

# Generate a presigned URL
aws s3 presign "s3://$BUCKET_NAME/$LOCAL_FILE" --expires-in "$EXPIRATION"

