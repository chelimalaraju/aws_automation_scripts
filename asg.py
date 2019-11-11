import boto3
asg_client = boto3.client("autoscaling")
asgnl = ['SSM-Testing']
for asgn in asgnl:
    resp = asg_client.suspend_processes(AutoScalingGroupName=asgn)
