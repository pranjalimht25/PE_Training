import json
import pymysql
import boto3
import datetime


def lambda_handler(event, context):
    client = boto3.client('dynamodb')
    response = client.scan(
        TableName='A2Q2_Temp',
        Select='ALL_ATTRIBUTES'
    )
    REGION = 'us-east-1'
    rds_host = "a2q2database.csaruqlxxway.us-east-1.rds.amazonaws.com"
    name = "a2q2user"
    password = "a2q2Userpass"
    db_name = "aquser"
    n = response['Count']
    for i in range(n):
        DB_id = int(response['Items'][i]['ID']['N'])
        DB_gender= response['Items'][i]['Gender']['S']
        DB_dt= response['Items'][i]['Dt']['S']
        if (DB_gender == 'F'):
            DB_gender = 'Female'
        else:
            DB_gender = 'Male'
        DB_dt = datetime.datetime.strptime(DB_dt, "%m/%d/%y").strftime("%d/%m/%Y")
        conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=10)
        with conn.cursor() as cur:
          #  cur.execute("create table a2q2table (Sid int primary key, Sgender varchar(255), Sdate varchar(255))")
            cur.execute("insert into a2q2table (Sid,Sgender,Sdate) values(%d, %s , %s)" %(DB_id,DB_gender,DB_dt))
            #cur.execute("select * from a2q2table")
            conn.commit()
            cur.close()
    return {
       'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }






