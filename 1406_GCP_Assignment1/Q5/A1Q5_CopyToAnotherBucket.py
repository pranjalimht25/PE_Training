from google.cloud import storage

def copy_object_to_new_bucket(bucket_name, src_obj, new_bucket_name, dest_obj):
    storage_client = storage.Client.from_service_account_json(
        "C:/GCP_A1Q5/cred.json"
    )
    source_bucket = storage_client.get_bucket(bucket_name)
    source_blob = source_bucket.blob(src_obj)
    destination_bucket = storage_client.get_bucket(new_bucket_name)

    new_blob = source_bucket.copy_blob(
        source_blob, destination_bucket, dest_obj)

    print('Blob {} in bucket {} copied to blob {} in bucket {}.'.format(
        source_blob.name, source_bucket.name, new_blob.name,
        destination_bucket.name))


def main():
    Src_Bucket_name = input("Enter Source Bucket name:")
    Dest_Bucket_name = input("Enter Destination Bucket name:")
    source_object_name = "Sample1.txt"
    dest_obj_name = "Sample_dest.txt"
    copy_object_to_new_bucket(Src_Bucket_name,source_object_name,Dest_Bucket_name,dest_obj_name)

main()