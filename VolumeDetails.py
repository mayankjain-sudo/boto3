from collections import defaultdict

import boto3
import csv
import time

ec2 = boto3.resource('ec2', region_name='ap-south-1')
volumes = ec2.volumes.all()
# print(volumes)
volumesinfo = defaultdict()
for volume in volumes:
    volumesinfo[volume.id] = {
        'Volume ID': volume.id,
        'Size': volume.size,
        'Created': volume.create_time,
        'State': volume.state,
        'Volume Type': volume.volume_type,
        'Availability Zone': volume.availability_zone,
        'Encrypted': volume.encrypted,
        'Iops': volume.iops,
        'Snapshot': volume.snapshot_id,
        'Attachmentment Info': volume.attachments,
        'Tags': volume.tags
    }
attributes = ['Volume ID', 'Size', 'Created', 'State', 'Volume Type', 'Availability Zone', 'Encrypted', 'Iops',
              'Snapshot', 'Attachmentment Info', 'Tags']

for volume_id, volume in volumesinfo.items():
    dictof = {key: volume[key] for key in attributes}
    print(dictof)
    csv_file = "volumeInfo.csv"
    with open(csv_file, 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=attributes)
        writer.writeheader()
        writer.writerow(dictof)
