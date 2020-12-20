import boto3
import csv
import time

boto3 = boto3.session.Session(region_name='ap-south-1')
ec2 = boto3.client('ec2')

with open('snapshots.csv', 'w') as csvfile:
    fields = ['Description', 'Encrypted','VolumeId','State','SnapshotId','VolumeSize','StartTime']
    writer = csv.writer(csvfile)
    writer.writerow(fields)

    page_iterator = ec2.get_paginator('describe_snapshots').paginate(OwnerIds=['self'])

    for page in page_iterator:
        for snapshot in page['Snapshots']:
            temp = [snapshot['Description'],snapshot['Encrypted'],snapshot['VolumeId'],snapshot['State'], snapshot['SnapshotId'], snapshot['VolumeSize'], snapshot['StartTime']]
            writer.writerows([temp])

csvfile.close()