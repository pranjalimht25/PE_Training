import boto3

def SecondLatestV(bucket,file):
        s3=boto3.client('s3')
        versions = s3.list_object_versions(Bucket = bucket, Prefix = file)
        s3.download_file(bucket, file ,'SecondLatestV.pdf', ExtraArgs={'VersionId':versions['Versions'][1]['VersionId']})
#Saving the File as "SecondLatestV" , this can be replaced by the desired location to save
#Used Index [1] to get the second latest Version

def main():
 bucket = "assignment1p"
 file= "pe_assignment_pranjali-1557764010908.pdf"
 SecondLatestV(bucket,file)

if __name__ == '__main__':
 main()