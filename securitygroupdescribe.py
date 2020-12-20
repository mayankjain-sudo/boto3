import boto3
import pandas as pd
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

try:
    response = ec2.describe_security_groups(GroupIds=['sg-033d57591a207071b'])
    #print(response)
    data = response.get("SecurityGroups")
    # print(data)
    ami_list = []
    for rawami in data:
        # print(rawami)
        ami_list.append(rawami)
    #print(ami_list)
    result_list = []
    for temp in ami_list:
        dict_keys = temp.keys()
        # print(dict_keys)
        temp_row = []
        for temp_key in dict_keys:
            temp_row.append(temp[temp_key])
        # print(temp_row)
        # print(temp_row)
        result_list.append(temp_row)
    # print(result_list)
    df = pd.DataFrame(result_list,columns=dict_keys)
    print(df)
    df.to_csv("SGDetails.csv", index=False)
except ClientError as e:
    print(e)