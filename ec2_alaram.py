import boto3
import collections

#Create Session with IAM User
session = boto3.session.Session(aws_access_key_id='ACCESS_KEY', aws_secret_access_key='ACCESS_KEY_SECRET')

ec2_sns = '<SNS_TOPIC_ARN>'

name_tag_equal = "something"

#Create AWS clients
ec = session.client('ec2')
cw = session.client('cloudwatch')
       
#Enumerate EC2 instances
reservations = ec.describe_instances().get('Reservations', [])
instances = sum(
    [
        [i for i in r['Instances']]
        for r in reservations
    ], [])

for instance in instances:
    try:
        for tag in instance['Tags']:
            if tag['Key'] == 'Name':
                name_tag = tag['Value']
                print "Found instance %s with name %s" % (instance['InstanceId'], name_tag)            
        #Create CPU Credit Alarms
        if name_tag == name_tag_equal:
            #Create Metric "CPU Credit Balance >= 95 for 10 Minutes"
            response = cw.put_metric_alarm(
                AlarmName="%s %s Credit Balance Warning" % (name_tag, instance['InstanceId']),
                AlarmDescription='CPU Credit Balance >= 95 for 10 Minutes',
                ActionsEnabled=True,
                AlarmActions=[
                    ec2_sns,
                ],
                MetricName='CPUCreditBalance',
                Namespace='AWS/EC2',
                Statistic='Average',
                Dimensions=[
                    {
                        'Name': 'InstanceId',
                        'Value': instance['InstanceId']
                    },
                ],
                Period=300,
                EvaluationPeriods=2,
                Threshold=95.0,
                ComparisonOperator='GreaterThanOrEqualToThreshold'
            )
    except Exception as e:
        print ("Error Encountered.")
        print (e)