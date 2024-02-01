import boto3
from botocore.exceptions import ClientError

# Create an S3 resource and client
s3_resource = boto3.resource('s3')
s3_client = boto3.client('s3')

# List of bucket names to delete (Replace 'demo1', 'demo2', ..., 'demoN' with actual bucket names)
buckets_to_delete = [
    'demo1',
    'demo2',
    # Add more bucket names as needed
    'demoN'
]

def empty_and_delete_bucket(bucket_name):
    try:
        # Emptying the bucket
        bucket = s3_resource.Bucket(bucket_name)
        bucket.objects.all().delete()

        # Deleting the bucket
        s3_client.delete_bucket(Bucket=bucket_name)
        print(f"Bucket {bucket_name} emptied and deleted successfully.")
    except ClientError as e:
        print(f"Error: {e.response['Error']['Message']}")

for bucket in buckets_to_delete:
    empty_and_delete_bucket(bucket)
