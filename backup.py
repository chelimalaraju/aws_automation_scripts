import boto3
import pprint
import encodings.idna
import pdb
regions = ["eu-west-1", "sa-east-1", "us-east-1", "ap-northeast-1", "us-west-2", "us-west-1", "ap-southeast-1", "ap-southeast-2"]
def lambda_handler(event,context):
    for i in regions:
        temp_backup = []
        ec2_client = boto3.client('ec2', region_name=i)
        ec2_des = ec2_client.describe_instances()
        for i in ec2_des['Reservations']:
            #pprint.pprint(i)
            for j in i['Instances']:
                #pprint.pprint(j)
                del temp_backup[:]
                pprint.pprint(j)
                if 'Tags' in j:
                    for k in j['Tags']:
                        temp_backup.append(k['Key'])
                    #print temp_backup
                    if 'gig-backup' in temp_backup:
                        print "Already backup tag is placed "+j['InstanceId']
                    else:
                        print "No backup tag is placed"+j['InstanceId']
                        response = ec2_client.create_tags(Resources=[j['InstanceId']], Tags=[{ 'Key': 'gig-backup', 'Value': '7d3w2m' }])
                        print "Now backup tag is placed"+j['InstanceId']
                    if 'monitoring' in temp_backup:
                        print "Already monitoring tag is placed "+j['InstanceId']
                    else:
                        print "No monitoring tag is placed"+j['InstanceId']
                        response = ec2_client.create_tags(Resources=[j['InstanceId']], Tags=[{ 'Key': 'monitoring', 'Value': 'on' }])
                        print "Now monitoring tag is placed"+j['InstanceId']
                else:
                    response = ec2_client.create_tags(Resources=[j['InstanceId']], Tags=[{ 'Key': 'monitoring', 'Value': 'on' }, { 'Key': 'gig-backup', 'Value': '7d3w2m' }])
