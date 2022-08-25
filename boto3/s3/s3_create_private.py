# importing boto3 library
import boto3

# definig boto3 resource in a variable.
aws_resource = boto3.resource('s3')
bucket = aws_resource.Bucket('cp-b00-boto3')


response = bucket.create(
    ACL='private',
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'
    },
    ObjectOwnership='ObjectWriter'
)
