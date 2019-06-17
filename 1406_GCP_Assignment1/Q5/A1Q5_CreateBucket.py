from google.cloud import storage


storage_client = storage.Client.from_service_account_json(
        "C:/GCP_A1Q5/cred.json"
)

#bucket_name = 'a1q5bucket'
bucket_name = input("Enter Bucket name :")
bucket = storage_client.create_bucket(bucket_name)
print('Bucket {} created.'.format(bucket.name))