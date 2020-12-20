import boto3
def lambda_handler(event, context):
    region = 'ap-south-1'
    client = boto3.client('ec2')
    #ec2_regions = [region['RegionName'] for region in client.describe_regions()['Regions']]
    #for region in ec2_regions:
    ec2 = boto3.resource('ec2',region_name=region)
    instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    RunningInstances = [instance.id for instance in instances]
    for i in RunningInstances:
        stoppingInstances = ec2.instances.stop(i)
        print(stoppingInstances)