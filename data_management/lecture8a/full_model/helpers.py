from json import dumps
import boto3
s3_resource = boto3.resource("s3")

def json_to_s3(uri, name, data):
    """
    Transfer a nested python object into s3 with boto
    """
    content = dumps(data)
    bucket =  s3_resource.Bucket(uri)
    object = bucket.Object(name)
    object.put(Body=content)