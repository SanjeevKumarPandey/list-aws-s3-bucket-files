# A simple script to list all contents of an AWS S3 bucket
# Sanjeev Pandey

from boto.s3.key import Key
import boto.s3.connection
import json
import boto3

# # Test Bucket
AWS_ACCESS_KEY_ID=""
AWS_SECRET_ACCESS_KEY=""
Bucketname="sample-bucket"


LOGFILE="S3FileList"+Bucketname+'.log'
ACLFILE="ACL-"+Bucketname+'.log'

# File operations
def printLogs(filename, data):
    with open(filename, 'a') as f:
        f.write(data+"\n")
        f.close()

# List files
conn = boto.s3.connect_to_region('ap-south-1',
       aws_access_key_id=AWS_ACCESS_KEY_ID,
       aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
       is_secure=True,               # uncomment if you are not using ssl
       calling_format = boto.s3.connection.OrdinaryCallingFormat(),
       )
bucket = conn.get_bucket(Bucketname)
for key in bucket.list():
    print (key.name)
    printLogs(LOGFILE,key.name)

# Init client for further flows
s3client=boto3.client('s3',aws_access_key_id=AWS_ACCESS_KEY_ID,
              aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

# Get bucket's ACL - Check Permissions
ACL=s3client.get_bucket_acl(Bucket=Bucketname)
printLogs(ACLFILE, json.dumps(ACL))

# Download File - Uncomment & modify to download a specific file
# s3client.download_file(Bucket=Bucketname,Key='sample-bucket/2020/07/small.mp4',Filename='./small.mp4')