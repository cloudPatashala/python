import boto3

aws_resource = boto3.resource('s3')
bucket = aws_resource.Bucket('cp-b00-boto3')

object = bucket.put_object(
    ACL='private',
    Body=b'This is test2',
    Key='test1',

)
