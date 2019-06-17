from google.cloud import storage

def upload_object(bucket_name, source_file_name, destination_blob_name):
    storage_client = storage.Client.from_service_account_json(
        "C:/GCP_A1Q5/cred.json"
    )
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))

def main():
    Bucket_name = input("Enter Bucket name:")
    source_file_path = "C:/GCP_A1Q5/Sample.txt"
    destination_name = "Sample_del.txt"
    upload_object(Bucket_name,source_file_path,destination_name)

main()