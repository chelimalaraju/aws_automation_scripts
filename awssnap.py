import boto3
import pprint
import pdb
from datetime import datetime
import datetime
temp2 = []
cutoff = datetime.datetime.utcnow() - datetime.timedelta(days=90)
DATEFORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'
ec2=boto3.client('ec2',region_name='us-east-1')
response = ec2.describe_images(Filters=[{'Name':'owner-id','Values': ['750434153990']}])
#pprint.pprint(response)
for d in response['Images']:
    c=d['CreationDate']
    #print c
    #pdb.set_trace()
    date_object = datetime.datetime.strptime(c, '%Y-%m-%dT%H:%M:%S.%fZ')
    print c
    print cutoff.strftime(DATEFORMAT)
    if (c < cutoff.strftime(DATEFORMAT)):
        img=d['ImageId']
        print 'This AMI is eligible to delete : '+img+' created on :'+c
        response2 = ec2.describe_images(Filters=[{'Name': 'image-id','Values': [img]}])
        #response1 = ec2.deregister_image(DryRun=False,ImageId=img)
        temp1=response2['Images'][0]['BlockDeviceMappings']
        for i in temp1:
            if 'Ebs' in temp1:
                temp2.append(i['Ebs']['SnapshotId'])
        for i in temp2:
            pass           
            #print i
            #response7 = ec2.delete_snapshot(DryRun=False, SnapshotId=i)
            #print response7
