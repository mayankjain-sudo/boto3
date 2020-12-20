import boto3
import csv
import time

boto3 = boto3.session.Session(region_name='ap-south-1')
ec2 = boto3.client('ec2')
#images = ec2.describe_images(Owners=['self'])

page_iterator = ec2.get_paginator('describe_images').paginate()

for page in page_iterator:
    for snapshot in page['Images']:
        print(snapshot['ImageId'])