import boto3

def copy_all_amis_owned_by_self_with_kms_encryption(source_region, destination_region):
    
    ec2 = boto3.client('ec2', region_name=source_region)
    
    # Get the list of AMIs in the source region.
    amis = ec2.describe_images(Owners=['self'])
    image_ids=[]
    # Copy the AMIs to the destination region.
    for ami in amis['Images']:
        image_ids.append(ami['ImageId'])
    print(image_ids)
    conn = boto3.client('ec2', region_name=destination_region)
    kms = boto3.client('kms', region_name=destination_region)
    key_id = 'ENTER YOUR KEY ID'
    arn = kms.describe_key(KeyId=key_id)['KeyMetadata']['Arn']

    for image_id in image_ids:
        destination_ami_id=conn.copy_image(
            Name=image_id,
            SourceImageId=image_id,
            SourceRegion=source_region,
            Encrypted=True,
            KmsKeyId=arn
        )
        
def main():
    """
    The main function of the script.
    """

    source_region = 'ap-south-1'
    destination_region = 'ap-southeast-1'

    copy_all_amis_owned_by_self_with_kms_encryption(source_region, destination_region)

if __name__ == '__main__':
    main()