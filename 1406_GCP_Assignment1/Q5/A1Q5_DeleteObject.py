from google.cloud import storage

def delete_obj(bucket_name, obj_name):
    storage_client = storage.Client.from_service_account_json(
        "C:/GCP_A1Q5/cred.json"
    )
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(obj_name)

    blob.delete()

    print('Object {} deleted.'.format(obj_name))


def main():
    Bucket_name = input("Enter Bucket name to delete object from:")
    Object_name = input("Enter Object name to delete:")
    delete_obj(Bucket_name,Object_name)

main()