import boto3
import requests

# ---- Configuration ----
bucket_name = "s3_bucket_lab.s3_upload.py"
object_name = "sample.gif"
file_url = "https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif"
expires_in = 3600  # seconds, 1 hour

# ---- Fetch file from the internet ----
response = requests.get(file_url)
with open(object_name, "wb") as f:
    f.write(response.content)

# ---- Upload file to S3 ----
s3 = boto3.client("s3")
s3.upload_file(object_name, bucket_name, object_name)

# ---- Generate presigned URL ----
url = s3.generate_presigned_url(
    "get_object",
    Params={"Bucket": bucket_name, "Key": object_name},
    ExpiresIn=expires_in
)

print("Presigned URL:", url)

