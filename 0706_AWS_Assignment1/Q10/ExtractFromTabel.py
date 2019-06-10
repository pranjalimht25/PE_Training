import boto3
import botocore
import os
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url="https://dynamodb.us-east-1.amazonaws.com")
table = dynamodb.Table('AGames')

print("Game with Gid as 2 is: ")

#Filter data based on Gid = 2
response = table.query(
    KeyConditionExpression=Key('gid').eq(2)
)

#Printing rating and game name of extracted element
for i in response['Items']:
    print(i['gname'], "and its rated :", i['rating'])