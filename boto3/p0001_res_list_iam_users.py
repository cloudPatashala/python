import boto3

# creating a management console session.
aws_mgmt_con = boto3.session.Session(profile_name="temp_user")

# Creating iam console session on top of aws management console session.
iam_con = aws_mgmt_con.resource('iam')

# print all iam users with a for loop.
for user in iam_con.users.all():
    print(user.name)
