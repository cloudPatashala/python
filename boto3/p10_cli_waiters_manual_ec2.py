import imp
from urllib import response
import boto3
from pprint import pprint
import sys
import time
aws_mgmt_con = boto3.session.Session(
    profile_name="temp_user", region_name="ap-south-1")

ec2_con_cli = aws_mgmt_con.client(service_name="ec2")

instance_id = "i-0c4286c6c2b31866a"


start_instance = ec2_con_cli.start_instances(
    InstanceIds=[instance_id]
)

'''stop_instance = ec2_con_cli.stop_instances(
    InstanceIds=[instance_id]
)'''


# pprint(response)
# pprint(response['Reservations'])
while True:
    response = ec2_con_cli.describe_instances(InstanceIds=[instance_id])
    for instances in response['Reservations']:
        for instance in instances['Instances']:
            instance_state = instance['State']
            print("\nThe ec2 instances state is " + instance_state['Name'])
    if instance_state['Name'] == "running":
        break
    print("Waiting for the instance to start....")
    time.sleep(5)
