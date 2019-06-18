from google.cloud import vision
from google.cloud.vision import types

#Code to extract details of image uploaded in the bucket using Cloud Vision API
def detect_labels(uri):
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = uri

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')
    print(labels)
	
        
def hello_gcs(event, context):
    #Using the name of the bucket attached to the cloud function, as cloud function gets triggered on addition of object(image) to this bucket
    uri_path = "gs://a2q5bucket/" + event['name']
    detect_labels(uri_path)
    
