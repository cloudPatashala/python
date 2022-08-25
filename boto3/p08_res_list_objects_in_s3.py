from urllib import response
import boto3
from pprint import pprint
aws_mgmt_con = boto3.session.Session(profile_name="temp_user")

s3 = aws_mgmt_con.resource(service_name="s3")

buckets = s3.buckets.all()

for bucket in buckets:
    # print(bucket.name)
    # pprint(dir(bucket.objects))
    # print(dir(bucket.objects.all()))
    for file in bucket.objects.all():
        # print(file.key)
        # print(dir(file))
        # print(type(file.storage_class))
        # print(type(file.size))
        size_in_kb = round(file.size/1024, 2)
        print("The file " + file.key + " in bucket " + bucket.name + " has " +
              file.storage_class + " storage class and its size is " + str(size_in_kb))
