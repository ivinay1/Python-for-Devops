# step 1 is to import boto 3
import boto3

# create a client for service u want to interact
client = boto3.client('s3');

#  to create bucket
# response = client.create_bucket( 
#     Bucket='vinay-botto3-demo-123',
#     CreateBucketConfiguration={
#         'LocationConstraint': 'eu-north-1'
#     }
# )

# to get bucket acl
# response = client.get_bucket_acl(
#     Bucket='vinay-botto3-demo-123'
# )

# to manipulate the response u need to convert it first to dict then perform action
# print(response)

#  To delete bucket
response = client.delete_bucket(
    Bucket='vinay-botto3-demo-123'
)