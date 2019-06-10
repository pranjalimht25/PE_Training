from __future__ import print_function
import os
import botocore.session

region = os.environ.get('AWS_DEFAULT_REGION', 'us-east-1')

session = botocore.session.get_session()
dynamodb = session.create_client('dynamodb', region_name=region)

table_name = "AGames"

#Creating Table with "gid" as partition key and rest of the fields can be added while putting items to table
params = {
    'TableName' : table_name,
    'KeySchema': [
        { 'AttributeName': "gid", 'KeyType': "HASH"}
    ],

    'AttributeDefinitions': [
        { 'AttributeName': "gid", 'AttributeType': "N" },
    ],

    'ProvisionedThroughput': {
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
}

# Create the table
dynamodb.create_table(**params)

# Wait for the table to exist before exiting
print('Waiting for', table_name, '...')
waiter = dynamodb.get_waiter('table_exists')
waiter.wait(TableName=table_name)
