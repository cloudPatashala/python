import boto3

from pprint import pprint

aws_mgmt_con = boto3.session.Session(
    profile_name="temp_user", region_name="ap-south-1")

ec2 = aws_mgmt_con.resource(service_name="ec2")

response = ec2.instances.all()

pprint(response)
for each_instance in response:
    # print(dir(each_instance))
    pprint(dir(each_instance))

    pprint(dir(each_instance.state))
    print("-------------------------------------")
    # print(dir(each_instance.state))
    # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    # print(each_instance.state.values.Name)
    print("The instance id is : {}\nThe AMI used is : {}\nThe instance State is : {}".format(
        each_instance.instance_id, each_instance.image_id, each_instance.state["Name"]))
