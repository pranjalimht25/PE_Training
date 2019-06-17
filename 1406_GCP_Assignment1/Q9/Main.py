import base64
from google.cloud import bigquery

def hello_pubsub(event, context):
    message = base64.b64decode(event['data']).decode('utf-8')
    message_list = message.splitlines()
    # Prerequisite : Message contains Bucket name and object path in different lines
    bucket_name = message_list[0]
    object_path = message_list[1]
    print(bucket_name)
    print(object_path)
    client = bigquery.Client()
    # dataset_id = 'pe-training:gcpdataset'
    dataset_ref = client.dataset('gcpdataset')
    job_config = bigquery.LoadJobConfig()

    job_config.autodetect = True

    job_config.source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON
    # Specifying the path to load the object
    uri = "gs://" + bucket_name + "/" + object_path
    load_job = client.load_table_from_uri(uri, dataset_ref.table("gcptable"), job_config=job_config)

