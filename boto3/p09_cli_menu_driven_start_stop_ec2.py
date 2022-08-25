import boto3
import sys

aws_mgmt_con = boto3.session.Session(
    profile_name="temp_user", region_name="ap-south-1")

ec2_con_cli = aws_mgmt_con.client(service_name="ec2")

while True:
    print("\n\nThis script will provide you basic option to be performed on EC2 instance.. ")
    print("""
	1. Start
	2. Stop
	3. Reboot
	4. Terminate
	5. Exit""")
    user_input = int(
        input("\nplease select the nuber of you action. like '1' for Start "))
    if user_input == 1:
        instance_id = str(input("\nPlease enter the instance id: "))
        print("\nStarting the EC2 Instance " + instance_id + " ...")
        response_start = ec2_con_cli.start_instances(
            InstanceIds=[instance_id]
        )

    elif user_input == 2:
        instance_id = str(input("\nPlease enter the instance id: "))
        print("\nStopping the EC2 instance" + instance_id + " ....")
        response_stop = ec2_con_cli.stop_instances(
            InstanceIds=[instance_id]
        )

    elif user_input == 3:
        print("\nRebooting the ec2 instance.....")

    elif user_input == 4:
        instance_id = str(input("\nPlease enter the instnace id: "))
        print("\nTerminating the EC2 instance.....")
        response = ec2_con_cli.terminate_instances(
            InstanceIds=[instance_id]
        )

    elif user_input == 5:
        print("\nExitting the script !")
        sys.exit()
    else:
        print("\nYour choice does not matach any actoin mentioned above: ")
