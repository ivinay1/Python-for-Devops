import boto3

ec2_client = boto3.client("ec2")

# Creating instance 

instance = ec2_client.run_instances(
    ImageId='ami-0aba19e56f3eaec05',  # Replace with a valid AMI ID for your region
    MinCount=1,
    MaxCount=1,
    InstanceType='t3.micro',
    KeyName='test-ec2-instance',
    SecurityGroupIds=['sg-05f9ec5d7558d14c6'],
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'Boto3_test_ec2_v2'
                },
                {
                    'Key': "Enviroment",
                    'Value': 'Test'
                }
            ]     
        }
    ]
)

print(instance['Instances'][0]['InstanceId'])


# Deleting instance
response = ec2_client.terminate_instances(
    InstanceIds=[
        'i-0eccb43298090aeb1',
        'i-0ed0364269a6b779d'
    ],
)

print(response)