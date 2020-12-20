from collections import defaultdict
import pandas as pd
import boto3
import csv
import time

ec2 = boto3.resource('ec2')

# Get information for all running instances
running_instances = ec2.instances.filter(Filters=[{
    'Name': 'instance-state-name',
    'Values': ['stopped']}])

ec2info = defaultdict()
for instance in running_instances:
    for tag in instance.tags:
        if 'Name'in tag['Key']:
            name = tag['Value']
    # Add instance info to a dictionary
    ec2info[instance.id] = {
        'Name': name,
        'Type': instance.instance_type,
        'State': instance.state['Name'],
        'Private IP': instance.private_ip_address,
        'Public IP': instance.public_ip_address,
        'VPC ID' : instance.vpc_id,
        'Instance ID': instance.instance_id,
        'Launch Time': instance.launch_time,
        'Security Groups' : instance.security_groups,
        'ImageId' : instance.image_id,
        'Platform': instance.platform,
        'BlockDeviceMappings' : instance.block_device_mappings,
        'EBS-optimized' : instance.ebs_optimized,
        'Subnet ID' : instance.subnet_id,
        'Tags' : instance.tags
        }
#print (ec2info)
attributes = ['Name', 'Type', 'State', 'Private IP', 'Public IP', 'VPC ID', 'Instance ID', 'Launch Time','Security Groups', 'ImageId','Platform','BlockDeviceMappings',
              'EBS-optimized','Subnet ID','Tags']
dict_list = []
for instance_id, instance in ec2info.items():
      dictof = { key : instance[key] for key in attributes}
      dict_list.append(dictof)
      
print(dict_list)
result_list = []
for temp in dict_list:
    dict_keys = temp.keys()
  
    temp_row = []
    for temp_key in dict_keys:
        temp_row.append(temp[temp_key])
    
    result_list.append(temp_row)
    #print("**************************************************************************")
df = pd.DataFrame(result_list,columns=dict_keys)
df.to_csv("inventoryNCCLstop23sept.csv", index=False)


