import boto3
import sys
from pprint import pprint

aws_mgmt_con = boto3.session.Session(
    profile_name="temp_user", region_name="ap-south-1")

ec2_con_re = aws_mgmt_con.resource(service_name="ec2")

while True:
    print("""Chose one of the below Options number
	1. Start
	2. Stop
	3. Terminate
	4. Reboot
	5. Exit
	""")
    user_input = int(input("Please select option number from above list: "))
    if user_input == 1:
        print("Starting ....")
        instance_id = str(input("Please enter instance id: "))
        instance = ec2_con_re.Instance(instance_id)
        # pprint(dir(instance)) ## use this to know the list of available option on instance object created in above line.
        instance.start()

    elif user_input == 2:
        print(" Stopping ....")
        instance_id = str(input("Please enter instance id: "))
        instance = ec2_con_re.Instance(instance_id)
        # pprint(dir(instance)) ## use this to know the list of available option on instance object created in above line.
        instance.stop()

    elif user_input == 3:
        print(" Terminating ...")
        instance_id = str(input("Please enter instance id: "))
        instance = ec2_con_re.Instance(instance_id)
        # pprint(dir(instance)) ## use this to know the list of available option on instance object created in above line.
        instance.terminate()
    elif user_input == 4:
        print(" Rebooting .....")
    elif user_input == 5:
        print("Exiting from the control...")
        sys.exit()
    else:
        print("Option selected is not correct, try again : ")
