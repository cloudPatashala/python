import boto3

s3_bucket = boto3.resource("s3")

response = s3_bucket.create_bucket(
    ACL='public-read',
    Bucket='cp-boto3-00',
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'
    },
    ObjectLockEnabledForBucket=False,
    ObjectOwnership='ObjectWriter'
)
