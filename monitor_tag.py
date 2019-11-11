import boto3

region='us-west-2'
def lambda_handler(event, context):
    ec2=boto3.client('ec2',region_name=region)
    reservations = ec2.describe_instances().get('Reservations', [])
    instances = sum([[i for i in r['Instances']]for r in reservations], [])
    for instance in instances:
        response = ec2.create_tags(Resources=[instance['InstanceId']],Tags=[{'Key': 'monitoring','Value': 'on'}])

    elb=boto3.client('elb')
    loadbalancers = elb.describe_load_balancers().get('LoadBalancerDescriptions', [])
    for loadbalancer in loadbalancers:
        response = elb.add_tags(LoadBalancerNames=[loadbalancer['LoadBalancerName'],],Tags=[{'Key': 'monitoring','Value': 'on'},])

    asg=boto3.client('autoscaling')
    autoscalinggroups = asg.describe_auto_scaling_groups().get('AutoScalingGroups', [])
    for autoscalinggroup in autoscalinggroups:
        response = asg.create_or_update_tags(Tags=[{'ResourceId': autoscalinggroup['AutoScalingGroupName'],'Key': 'monitoring','Value': 'on','ResourceType': 'auto-scaling-group','PropagateAtLaunch': True,},])

    rds=boto3.client('rds')
    rdsinstances = rds.describe_db_instances().get('DBInstances', [])
    acc_no = ec2.describe_security_groups()['SecurityGroups'][0]['OwnerId']
    for rdsinstance in rdsinstances:
        response = rds.add_tags_to_resource(ResourceName='arn:aws:rds:'+region+':'+acc_no+':db:'+rdsinstance['DBInstanceIdentifier'], Tags=[{'Key': 'monitoring','Value': 'on'},])

