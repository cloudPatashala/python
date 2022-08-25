import boto3

# creating a management console session.
aws_mgmt_con = boto3.session.Session(profile_name="temp_user")

# Creating iam console session on top of aws management console session.
s3_con = aws_mgmt_con.resource('s3')

# print all s3 bucket names with a for loop.
for each_bucket in s3_con.buckets.all():
    print(each_bucket.name)
