import boto3

aws_mgmt_con = boto3.session.Session(
    profile_name="temp_user", region_name="ap-south-1")

ec2_con_res = aws_mgmt_con.resource(service_name="ec2")

print(ec2_con_res.meta.client.describe_regions()['Regions'])


for each in ec2_con_res.meta.client.describe_regions()['Regions']:
    print(each['RegionName'])
