import boto3
dynamoDb = boto3.resource('dynamodb')
dynamoTable = dynamoDb.Table ('AGames')

#code to put items to table
dynamoTable.put_item(
Item =
{
    'gid': 1,
    'gname': "COC",
    'publisher': "QWERTY publisher",
    'rating': 4,
    'release_date': "21-01-2016",
    'genres': ["G1", "G2"]
}

)