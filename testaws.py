import pprint
import boto3
import datetime
region='us-west-2'
ec2=boto3.client('ec2',region_name=region)
#instances = ec2.describe_instances()
#list1 = []
#list2 =[]
#AMI_LIST = []
#response = []
DATEFORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'
cutoff = datetime.datetime.utcnow() - datetime.timedelta(days=90)
cutoff1 = datetime.datetime.strptime(str(cutoff), '%Y-%m-%d %H:%M:%S.%f').strftime('%y, %m, %d')
#reserv=len(instances['Reservations'])
#print reserv
response = ec2.describe_images(Filters=[{'Name':'owner-id','Values': ['8888888888']}])
for d in response['Images']:
	c=d['CreationDate']
	actual_date = datetime.datetime.strptime(str(c), '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%y, %m, %d')
	if actual_date < cutoff1:
	 	response1 = ec2.describe_instances(Filters=[{'Name':'image-id','Values': [d['ImageId']]}])
	 	if len(response1['Reservations'])>0:
	 		for k in response1['Reservations']:
				temp = k['Instances'][0]['InstanceId']
				print 'Instance is attached to the AMI : '+d['ImageId']
				print (d['ImageId']+':'+d['VirtualizationType']+':'+d['CreationDate']+':'+d['Name']+':'+region+':'+temp)
				print "*********************Instace ids and states***************"
				print 'instace id ' + temp + ' is ' + k['Instances'][0]['State']['Name']
		else:
			print 'No instance is attached to this AMI'+d['ImageId']
			print (d['ImageId']+':'+d['VirtualizationType']+':'+d['CreationDate']+':'+d['Name']+':'+region)
			img=d['ImageId']
	        print 'This AMI is eligible to delete : '+img+' created on :'+c
	        response2 = ec2.describe_images(Filters=[{'Name': 'image-id','Values': [img]}])
	        print "***********You are eligible to delete this image id**************" + img
	        #response1 = ec2.deregister_image(DryRun=False,ImageId=img)
	        temp1=response2['Images'][0]['BlockDeviceMappings']
	        for i in temp1:
	            if 'Ebs' in temp1:
	                temp2.append(i['Ebs']['SnapshotId'])
	        for i in temp2:
	            pass
	            print "--------------You are eligible to delete this snapshot id -------------" + i
	            #print i
	            #response7 = ec2.delete_snapshot(DryRun=False, SnapshotId=i)
	            #print response7