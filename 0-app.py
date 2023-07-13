import csv 
import boto3


s3 = boto3.resource(
    service_name='s3',
    region_name='ap-south-1',
    aws_access_key_id='AKIAZUNUBXQQW72HSRFD',
    aws_secret_access_key='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'
)

bucket_name = 'ckyc-syn-uat'

filename = "total-s3images-140423.csv"

fields = ['name', 'size'] 
with open(filename, 'a', newline='') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    for obj in s3.Bucket(bucket_name).objects.all():
        obj_resource = s3.Object(bucket_name, obj.key)
        csvwriter.writerow([obj.key, obj_resource.content_length])