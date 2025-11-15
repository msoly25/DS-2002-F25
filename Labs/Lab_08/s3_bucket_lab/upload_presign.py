import boto3

# 1. S3 client
s3 = boto3.client('s3', region_name='us-east-1')

# 2. File info
bucket_name = 'ds2002-f25-uth7hq'
s3_key = 'uploads/heart.png'  # must match upload path
expires_in = 3600             # 1 hour in seconds

# 3. Generate presigned URL
url = s3.generate_presigned_url(
    ClientMethod='get_object',
    Params={'Bucket': bucket_name, 'Key': s3_key},
    ExpiresIn=expires_in
)

print(f"Presigned URL (valid for {expires_in} seconds):")
print(url)

