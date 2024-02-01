import boto3
from botocore.exceptions import ClientError

# Create an S3 resource and client
s3_resource = boto3.resource('s3')
s3_client = boto3.client('s3')

# List of bucket names to delete
buckets_to_delete = [
    'amity-university-data-symposium-2023',
    'anyname-12345678909',
    'aws-athena-query-results-us-east-1-823711539498',
    'aws-prepration',
    'cf-templates-17cp81ostdnn1-us-east-1',
    'codepipeline-us-east-1-972276161789',
    'dev-manik-project',
    'elasticbeanstalk-ap-southeast-1-823711539498',
    'elasticbeanstalk-us-east-1-823711539498',
    'ingram-presentation',
    'manikgpt-k8s-cluster',
    'meena-kumari',
    'prod-manik-project',
    'qs-ml-blog-data-athena-output',
    'serverless-batch-artifact-bucket',
    'serverless-batch-data-bucket',
    'uat-manik-project',
    'varunmanik-uniquevalue1',
    'varunmanik-uniquevalue123'
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