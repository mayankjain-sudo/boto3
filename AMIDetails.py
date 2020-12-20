from collections import defaultdict
import pandas as pd
import boto3
import csv
import time

client = boto3.client('ec2')

images = client.describe_images(Owners=['self'])
#images = client.describe_images()
#print(images)
data = images.get("Images")
#print(data)
ami_list = []
for rawami in data:
    #print(rawami)
    ami_list.append(rawami)
#print(ami_list)
result_list = []
for temp in ami_list:
    dict_keys = temp.keys()
    #print(dict_keys)
    temp_row = []
    for temp_key in dict_keys:
        temp_row.append(temp[temp_key])
    #print(temp_row)
    #print(temp_row)
    result_list.append(temp_row)
print(result_list)
df = pd.DataFrame(result_list,columns=dict_keys)
#print(df)
df.to_csv("AMIDetails.csv", index=False)