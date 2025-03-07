from json import dumps, load
from minio import Minio
from minio.error import S3Error
import io

def make_client(configfile):
    data = {
        "endpoint": "localhost",
        "access_key": NULL,
        "secret_key": NULL
    }

    with open(configfile, 'r') as file:
        data = json.load(file)

    client = Minio(data["endpoint"], access_key=data["access_key"], secret_key=data["secret_key"])
    return client

s3_resource = make_client("s3.json")

def json_to_s3(uri, name, data):
    found = client.bucket_exists(uri)
    if not found:
        client.make_bucket(uri)
   
    content = io.BytesIO(dumps(data))
    client.put_object(uri, name, content, len(content))