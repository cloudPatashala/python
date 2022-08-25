import boto3

aws_mgmt_con = boto3.session.Session(profile_name="temp_user")

s3_con = aws_mgmt_con.client(service_name="s3")

response = s3_con.list_buckets()
print(response)
print("-------------------------------------------------------")
for each_buck in response['Buckets']:
    print(each_buck['Name'], each_buck['CreationDate'])
