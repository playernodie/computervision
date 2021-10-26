import sys
import boto3
from botocore.config import Config
import requests
import os
import numpy as np
from os.path import exists

print(boto3.__version__)
s3 = boto3.client('s3', config=Config(signature_version='s3v4',region_name='us-east-2'))
S3_UPLOAD_BUCKET='pulic-upload'

def presign_link_s3_put_obj(bucket, file_name,expiration):
  if file_name==None:
      raise Exception("Sorry, file name is None") 
  url = s3.generate_presigned_url(ClientMethod='put_object', Params={'Bucket': bucket,'Key': file_name},ExpiresIn=expiration)
  return url

def presign_link_s3_get_obj(bucket, file_name, expiration):
  if file_name==None:
      raise Exception("Sorry, file name is None") 
  url = s3.generate_presigned_url(ClientMethod='get_object', Params={'Bucket': bucket,'Key': file_name},ExpiresIn=expiration)
  return url

def upload_file_to_s3(file_name, bucket=S3_UPLOAD_BUCKET):
  name=os.path.basename(file_name)
  with open(file_name,'rb') as payload:
    return requests.put(presign_link_s3_put_obj(bucket, name, 60), 
                        data=payload,headers={'content-type': 'application/x-www-form-urlencoded'})

# default download file to current location
def download_file_from_s3(file_name,bucket=S3_UPLOAD_BUCKET,base_dir=''):
  s3_pre_sign_link= presign_link_s3_get_obj(bucket, file_name, 60)
  res=requests.get(s3_pre_sign_link)
  if res.status_code == 200: 
    with open(base_dir+file_name,'wb') as openfile:
      openfile.write(res.content)
  return res
