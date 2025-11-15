import boto3

print("boto3 imported successfully!")

# Step 4.3: Create S3 client
s3 = boto3.client('s3', region_name='us-east-1')

# Define bucket and file
bucket_name = 'ds2002-f25-uth7hq'
local_file = 'google_logo.png'
s3_key = 'google_logo.png'

# Upload file privately
with open(local_file, 'rb') as data:
    s3.put_object(
        Bucket=bucket_name,
        Key=s3_key,
        Body=data
    )

print(f"File {local_file} uploaded to {bucket_name}/{s3_key} privately.")

