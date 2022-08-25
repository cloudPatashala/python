import boto3

aws_mgmt_con = boto3.session.Session(profile_name="temp_user")

s3_con = aws_mgmt_con.resource('s3')

for each_buck in s3_con.buckets.all():
    print(each_buck)

#print(each_buck.name, each_buck.aws_region)
