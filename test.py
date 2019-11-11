'''
import boto3  
from datetime import datetime, timedelta  
region = "us-west-2"  
ec2 = boto3.resource("ec2", region_name=region)
instances = ec2.instances.filter(Filters=[{'Name': 'owner-id','Values': ['750434153990']}])
instances = [instance.id for instance in instances]
images = ec2.images.filter(Filters=[{'Name': 'owner-id','Values': ['750434153990']}])  
images = [image.id for image in images]  
snapshots = ec2.snapshots.filter(Filters=[{'Name': 'owner-id','Values': ['750434153990']}])
snapshots = [snapshot.id for snapshot in snapshots]
'''
import pprint
import boto3
import datetime
region='us-west-2'
ec2=boto3.client('ec2',region_name=region)
instances = ec2.describe_instances()
list1 = []
list2 =[]
AMI_LIST = []
response = []
DATEFORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'
cutoff = datetime.datetime.utcnow() - datetime.timedelta(days=3)
cutoff1 = datetime.datetime.strptime(str(cutoff), '%Y-%m-%d %H:%M:%S.%f').strftime('%y, %m, %d')
reserv=len(instances['Reservations'])
print reserv
response = ec2.describe_images(Filters=[{'Name':'owner-id','Values': ['750434153990']}])
for d in response['Images']:
	c=d['CreationDate']
	print c
	actual_date = datetime.datetime.strptime(str(c), '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%y, %m, %d')
	if actual_date < cutoff1:
	 	response1 = ec2.describe_instances(Filters=[{'Name':'image-id','Values': [d['ImageId']]}])
	 	if len(response1['Reservations'])>0:
	 		for k in response1['Reservations']:
				temp = k['Instances'][0]['InstanceId']
				print 'instance is attached to the AMI : '+d['ImageId']
				print (d['ImageId']+':'+d['VirtualizationType']+':'+d['CreationDate']+':'+d['Name']+':'+region+':'+temp)
	else:
		print 'NO instance is attached to this AMI'+d['ImageId']
		print (d['ImageId']+':'+d['VirtualizationType']+':'+d['CreationDate']+':'+d['Name']+':'+region)