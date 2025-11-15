import boto3

# 1. Create S3 client
s3 = boto3.client('s3', region_name='us-east-1')

# 2. Define bucket and file paths
bucket_name = 'ds2002-f25-uth7hq'
local_file = 'heart.png'       # local file path
s3_key = 'uploads/heart.png'   # path inside S3 bucket

# 3. Upload file (private, no ACLs)
s3.upload_file(
    Filename=local_file,
    Bucket=bucket_name,
    Key=s3_key
)

print(f"File {local_file} uploaded successfully to {bucket_name}/{s3_key}")

