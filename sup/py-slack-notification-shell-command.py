from distutils.log import debug
from email import message
from http import client
from lib2to3.pytree import HUGE
import os
import json
import threading
from time import sleep
from urllib import response
from webbrowser import get
import sys
from slack import WebClient
import subprocess
import re
import datetime

month_today = datetime.date.today()
month_start = datetime.date(month_today.year, month_today.month, 1)

# Slack API connection https://slack.dev/python-slackclient/basic_usage.html
slack_token = sys.argv[3]
client = WebClient(token=slack_token)

REALMS_TO_SELECT = ["ABCD"]

# Checking if the list of sandbox.json is existing or not
sandbox_list_filename = "sandbox_list.json"
if os.path.exists(sandbox_list_filename):
    print("file already exists. Deleting!")
    os.system(f"rm -rf {sandbox_list_filename}")


def execute_bash_command(bash_command):
    proc = subprocess.Popen([bash_command], stdout=subprocess.PIPE, shell=True)
    (out, error) = proc.communicate()
    return out

# #Authentication login


def authenticate_sandbox():
    client_id = sys.argv[1]
    client_password = sys.argv[2]
    auth_login_command = f"command client:auth {client_id} {client_password}"
    execute_bash_command(auth_login_command)


threading.Thread(target=authenticate_sandbox).start()
sleep(5)

# Get sandbox list
sandbox_list_command = f"command sandbox:list --json > {sandbox_list_filename}"
execute_bash_command(sandbox_list_command)

# Process the sandbox list file to get list of bdkj
realms_list = []
instances_list = []
id_list = []
ods_total_credits_used_tillnow = 0
slack_message_mindown_total_credits = []

with open(sandbox_list_filename, "r") as file:
    sandbox_instances = json.loads(file.read())
    for item in sandbox_instances:
        realm = item.get("realm")
        if realm in REALMS_TO_SELECT:
            id = item.get("id")
            instance = item.get("instance")
            realms_list.append(realm)
            instances_list.append(instance)
            id_list.append(id)


def handle_sandboxes(realms_list, instances_list, get, id_list):
    for realm, instance, id in zip(realms_list, instances_list, id_list):
        # Command Getting the access token
        sandbox_command_accesstoken = f"curl --location --request POST 'https://google.com' --header 'authorization: Basic ' --header 'content-type: application/x-www-form-urlencoded' | jq .access_token | tr -d '\"'"
        execute_bash_command(sandbox_command_accesstoken)
        sandbox_command_response3 = execute_bash_command(
            sandbox_command_accesstoken)
        accesstoken = sandbox_command_response3.decode('utf-8')
        access_token = accesstoken.strip()
        # Command getting the MinutesUp
        sandbox_instances_usage_minutesup = f"curl -X 'GET' 'https://google/api/v1/sandboxes/{id}/usage?from={month_start}&to={month_today}' -H 'accept: application/json' -H 'authorization: Bearer {access_token}'  | jq -r '.data | .minutesUp'"
        # Command getting the MinutesDown
        sandbox_instances_usage_minutesdown = f"curl -X 'GET' 'https://google/api/v1/sandboxes/{id}/usage?from={month_start}&to={month_today}' -H 'accept: application/json' -H 'authorization: Bearer {access_token}'  | jq -r '.data | .minutesDown'"
        sandbox_usage_response_minup = execute_bash_command(
            sandbox_instances_usage_minutesup)
        sandbox_usage_response_minup = sandbox_usage_response_minup.decode(
            'utf-8')
        sandbox_usage_response_mindown = execute_bash_command(
            sandbox_instances_usage_minutesdown)
        sandbox_usage_response_mindown = sandbox_usage_response_mindown.decode(
            'utf-8')
        print(sandbox_usage_response_minup)
        print(sandbox_usage_response_mindown)
        # Slack Messgae Format
        sandbox_command = f"echo '========================' && echo '\nUsage for {realm}-{instance} from {month_start} to {month_today}' && echo '\n-------------------------------------'"
        sandbox_command_response = execute_bash_command(sandbox_command)
        sandbox_command_response = sandbox_command_response.decode('utf-8')
        #sandbox_command_response = sandbox_command_response + '\n'+'-'* 50

        print("minutesUp : " + sandbox_usage_response_minup)
        print("minutesDown : " + sandbox_usage_response_mindown)

        print("ODS Sandbox Usage : " + sandbox_command_response)
        # Sending out Slack Notifications of ODS Sandbox Usage
        response = client.chat_postMessage(
            channel="XXXXXXX",
            text=sandbox_command_response
        )
        # Converting the ODS Minutes to Hours divided by 60
        sandbox_hours = int(sandbox_usage_response_minup) // 60
        slack_message_hours = f"ODS Sandbox Usage in Hours: {sandbox_hours}"
        print(f"ODS Sandbox Usage in Hours: {sandbox_hours}")
        # Sending out Slack Notifications of ODS Sandbox Hours
        response = client.chat_postMessage(
            channel="XXXXXXX",
            text=slack_message_hours
        )
        # Converting the ODS MinutesUp to Credits divided by 4
        sandbox_minup_credits = int(sandbox_usage_response_minup) // 4
        slack_message_minup_credits = f"ODS Sandbox Running Cost (Credits/Minute) : {sandbox_minup_credits}"
        response = client.chat_postMessage(
            channel="XXXXXXX",  # original channel id: XXXXXXX
            text=slack_message_minup_credits
        )
        # Converting the ODS MinutesDown to Credits multiplied by 0.3
        sandbox_mindown_credits = int(sandbox_usage_response_mindown) * 0.3
        slack_message_mindown_credits = f"ODS Sandbox Stopped Cost (Credits/Minute) : {sandbox_mindown_credits}"
        response = client.chat_postMessage(
            channel="XXXXXXX",
            text=slack_message_mindown_credits
        )

#         #Total Number of Credits
#         ods_total_credits_used = ods_total_credits_used_tillnow + int(sandbox_usage_response_minup)
#         slack_message_mindown_total_credits = f"Total ODS Sandbox Minutes Credits Used: {ods_total_credits_used}"

# #Sending out Slack Notifications of ODS Sandbox Usage Cost of Credits/Minutes
# response = client.chat_postMessage(
# channel = "XXXXX",  #original channel id: XXXXXXX
# text = slack_message_mindown_total_credits
#         )


# ODS Sandboxe Usage Command
handle_sandboxes(realms_list=realms_list,
                 instances_list=instances_list, get="get", id_list=id_list)

# Delete the sandbox list file
print("Deleting the sandbox list file!")
os.system(f"rm -rf {sandbox_list_filename}")

# for running list of bash commands
commands = []
for command in commands:
    os.sytem(command)
