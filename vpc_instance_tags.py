import boto3
vpc_id = 'vpc-82d36ee6'
ec2 = boto3.resource('ec2', region_name='us-west-2')
vpc = ec2.Vpc(vpc_id)
instances = vpc.instances.all()
t1 = 0
for i in instances:
    t2 = 0
    with open ('vpc_instances.txt','a') as vpc_seqf:
        if t1 == 0:
            vpc_seqf.write("{:30} {:30} {:30} {}".format('vpc_id', 'instance_id', 'tag_Key', 'tag_Value'))
            vpc_seqf.write("\n")
        if i.tags:
            for tag in i.tags:
                if t2 == 0:
                    vpc_seqf.write("\n")
                    vpc_seqf.write("{:30} {:30} {:30} {}".format(vpc_id, i.instance_id, tag['Key'], tag['Value']))
                else:
                    vpc_id = '     '
                    instance_id = '     '
                    vpc_seqf.write("{:30} {:30} {:30} {}".format(vpc_id, instance_id, tag['Key'], tag['Value']))
                vpc_seqf.write("\n")
                t1 = t1+1
                t2 = t2+1
        else:
            tag_Key = '     '
            tag_Value = '     '
            vpc_seqf.write("\n")
            vpc_seqf.write("{:30} {:30} {:30} {}".format(vpc_id, i.instance_id, tag_Key, tag_Value))
            t1 = t1+1
