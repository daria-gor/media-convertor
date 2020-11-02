import os
from minio import Minio
from minio.error import (ResponseError, BucketAlreadyOwnedByYou, BucketAlreadyExists)
import time

minioClient = Minio(os.getenv("S3_HOST")+":"+os.getenv("S3_PORT"),
                    access_key=os.getenv("MINIO_ACCESS_KEY"),
                    secret_key=os.getenv("MINIO_SECRET_KEY"),
                    secure=False)

try:
    minioClient.make_bucket("inbucket", location="eu-central-1"),
except BucketAlreadyOwnedByYou as err:
    pass
except BucketAlreadyExists as err:
    pass
except ResponseError as err:
    raise

try:
    minioClient.make_bucket("outbucket", location="eu-central-1"),
except BucketAlreadyOwnedByYou as err:
    pass
except BucketAlreadyExists as err:
    pass
except ResponseError as err:
    raise



def downloadingFromMinio(object):
    try:
        minioClient.fget_object('inbucket', object, '/tmp/'+object)
    except ResponseError as err:
        print(err)

def uploadToMinio(object):
    try:
        minioClient.fput_object('outbucket',object,'/tmp/'+object)
    except ResponseError as err:
        print(err)

def deletingFromMinio(object):
    try:
        minioClient.remove_object('inbucket',object)
    except ResponseError as err:
        print(err)

def ffmpegEngine(object):
    bitrate= os.getenv("BITRATE")
    in_pathfile = '/tmp/' + object
    out_pathfile = '/tmp/' + 't_' + object
    cmd = 'ffmpeg -y -i ' + in_pathfile + ' -codec:a libmp3lame -b:a '+ bitrate +' '+out_pathfile
    print(cmd)
    os.system(cmd)


# List all object paths in bucket that begin with my-prefixname.



objects = minioClient.list_objects_v2('inbucket', prefix='', recursive=True)


while objects != 0:
    objects = minioClient.list_objects_v2('inbucket', prefix='', recursive=True)

    for obj in objects:
        print(obj.object_name)
        downloadingFromMinio(obj.object_name)
        ffmpegEngine(obj.object_name)
        uploadToMinio('t_'+obj.object_name)
        deletingFromMinio(obj.object_name)

else:
    time.sleep(20)

