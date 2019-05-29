import json

filename = "S3Bucket.json"

#Read JSON data into the datastore variable
if filename:
    with open(filename, 'r') as f:
        datastore = json.load(f)


print(datastore["Records"][0]["s3"]["bucket"]["arn"])