from google.cloud import storage

def download_object(bucket_name, source_blob_name, destination_file_name):
    storage_client = storage.Client.from_service_account_json(
        "C:/GCP_A1Q5/cred.json"
    )
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)

    blob.download_to_filename(destination_file_name)

    print('Object {} downloaded to {}.'.format(
        source_blob_name,
        destination_file_name))


def main():
    Bucket_name = input("Enter Bucket name:")
    source_object_name = "Sample1.txt"
    destination_name = "Sample_downloaded.txt"
    download_object(Bucket_name,source_object_name,destination_name)

main()