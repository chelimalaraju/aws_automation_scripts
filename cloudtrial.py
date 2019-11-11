import boto3
regions = ["eu-west-1", "sa-east-1", "us-east-1", "ap-northeast-1", "us-west-2", "us-west-1", "ap-southeast-1", "ap-southeast-2"]
for i in regions:
    client = boto3.client('cloudtrail', region_name=i)
    response = client.describe_trails()
    for j in range(len(response['trailList'])):
        try:
            if response['trailList'][j]['IsMultiRegionTrail']==False:
                print 'cloud-Trail ' + response['trailList'][j]['Name'] + ' is enabled in region --> ' + i
                is_multi_region = raw_input('Do you want to enable the cloud trail ' + response['trailList'][j]['Name'] + ' for all regions (y/n)')
                if is_multi_region.lower() == 'y':
                    client.update_trail(Name=response['trailList'][j]['Name'], IsMultiRegionTrail=True)
            else:
                if (response['trailList'][j]['HomeRegion'] == i):
                    print 'cloud-Trail ' + response['trailList'][j]['Name'] + ' is enabled for all regions'
        except Exception as d:
            pass
