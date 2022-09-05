import boto3

aws_mgmt_con = boto3.session.Session(profile_name="temp_user")

ec2_con_res = aws_mgmt_con.resource(service_name="ec2")

filter_all_running_stopped = {
    "Name": "instance-state-name", "Values": ['running', 'stopped']}
filter_stopped_only = {
    "Name": "instance-state-name", "Values": ['stopped']
}

for each in ec2_con_res.instances.filter(Filters=[filter_all_running_stopped]):
    print("all instances are " + each.id)

for each in ec2_con_res.instances.filter(Filters=[filter_stopped_only]):
    print("Stopped instances are " + each.id)
