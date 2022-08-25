import boto3

aws_mgmt_con = boto3.session.Session(profile_name="temp_user")

ec2 = aws_mgmt_con.client(service_name="ec2", region_name="ap-south-1")

response = ec2.describe_instances()

print(response)
print("-------------------------------------------")

for each_ec2 in response['Reservations']:
    print(each_ec2['Instances'])
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    for e_i in each_ec2['Instances']:
        print(e_i['InstanceId'],
              e_i['ImageId'], e_i['PrivateIpAddress'], e_i['PublicIpAddress'], e_i['KeyName'], e_i['InstanceType'])
