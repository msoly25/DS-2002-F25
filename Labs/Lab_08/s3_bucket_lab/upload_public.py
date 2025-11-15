import boto3

# Create S3 client
s3 = boto3.client('s3', region_name='us-east-1')

bucket = 'ds2002-f25-uth7hq'  # your bucket name
local_file = 'heart.png'       # the same file, or another
s3_key = 'public/heart.png'    # path in S3 (can be different from private one)

s3.upload_file(
    Filename=local_file,
    Bucket=bucket,
    Key=s3_key,
    ExtraArgs={'ACL': 'public-read'}  # makes it public
)

print(f"File {local_file} uploaded to {bucket}/{s3_key} (public).")

