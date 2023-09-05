import boto3

AWS_REGION = "ca-central-1"

client = boto3.client("s3", region_name=AWS_REGION)

bucket_name = "BucketName"
location = {'LocationConstraint': AWS_REGION}

response = client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)

print("Amazon S3 bucket has been created")