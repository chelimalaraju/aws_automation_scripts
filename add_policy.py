import boto3
ec2_client = boto3.client('ec2')
iam_client = boto3.client('iam')
instances = ec2_client.describe_instances(Filters = [{'Name':'platform', 'Values':['windows']}])
print instances
for win_instance in instances['Reservations']:
    role = win_instance['Instances'][0]['IamInstanceProfile']['Arn'].split('/')[1]
    response_attach_role_policy = iam_client.attach_role_policy(RoleName=role,PolicyArn='arn:aws:iam::aws:policy/service-role/AmazonEC2RoleforSSM')
