from tkinter import E
from urllib import response
import boto3
from pprint import pprint

aws_mgmt_con = boto3.session.Session(
    profile_name="temp_user", region_name="ap-south-1")

s3 = aws_mgmt_con.client(service_name="s3")

# pprint(dir(s3))

response = s3.list_buckets()

for each_bucket in response['Buckets']:
    # print(each_bucket['Name'])
    bucket_name = each_bucket['Name']

    object_list = s3.list_objects_v2(Bucket=bucket_name)
    # pprint(object_list)
    # print("-----------------------------")
    # pprint(dir(object_list))
    for each_object in object_list['Contents']:
        files = each_object['Key']
        size = each_object['Size']
        last_modified = each_object['LastModified']

        print("Bucket: " + bucket_name + "\nFile name " + files +
              "\nSize : " + str(size) + "\nLast Modified on : " + str(last_modified))
        print("-----------------------------------")
